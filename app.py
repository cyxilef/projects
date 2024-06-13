from flask import Flask, render_template, request, redirect, session, url_for
from util import load_notes, load_users, save_users, save_notes, login, signup, add_note, remove_note, view_note, edit_note
from datetime import datetime

app = Flask(__name__)
app.secret_key = b'applesandbananas'

users = load_users()
notes = load_notes()
notes_json_string = load_notes()
logged_in = False
username = ""

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/signup", methods=["GET", "POST"])
def signup_page():
    global logged_in, username, users
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if signup(users, username, password):
            save_users(users)
            return redirect("/")
        else:
            return "Failed Signup"
    elif request.method == "GET":
        return render_template("signup.html")

@app.route("/login", methods=["GET", "POST"])
def login_page():
    global logged_in
    
    if logged_in:
        return redirect("/notes")
    
    if request.method == "POST":
        username = request.form['username']
        password = request.form['password']
        if login(users, username, password): 
            session['username'] = username
            logged_in = True
            user_notes = {title: note for title, note in notes.items() if note["author"] == username}
            if user_notes:
                return redirect("/notes")
            else:
                return redirect("/notes") 
        else:
            return "Wrong Username or Password, Please Try Again."
    elif request.method == "GET":
        return render_template("login.html")

@app.route("/notes", methods=["GET", "POST"])
def view_notes():
    global notes, logged_in

    if not logged_in:
        return redirect("/login") 

    if request.method == "POST":
        data = request.form
        title = data.get("title", "")
        description = data.get("description", "")
        labels = data.get("labels", "")
        author = data.get("author", "")
        note_type = data.get("note_type", "")
        current_datetime = datetime.now()
        timestamp = current_datetime.strftime('%Y-%m-%d %H:%M:%S')
        is_public = note_type == "public"
        is_private = note_type == "private"
        add_note(notes, title, description, author, labels, timestamp, is_public=is_public, is_private=is_private)
        save_notes(notes)
    
        return redirect("/notes")
    else:
        notes = load_notes()
    
        public_notes = {title: note for title, note in notes.items() if note.get('is_public')}
        private_notes = {title: note for title, note in notes.items() if not note.get('is_public') and note["author"] == session.get("username")}

        if session.get("username") is None:
            # If the user is not logged in, hide private notes
            private_notes = {}

        return render_template("notes.html", public_notes=public_notes, private_notes=private_notes)
        

@app.route("/note/<title>")
def get_note(title):
    global notes, logged_in
    note = view_note(notes, title)
    if note is None:
        return "Note not found", 404
    if note['is_public'] or (session.get("username") and note["author"] == session.get("username")):
        return render_template("note.html", note=note)
    elif session.get("username"):
        return "You are not authorized to view this note"
    else:
        return redirect("/login")

@app.route("/note/remove/<title>", methods=["POST"])
def remove_notes(title):
    global notes
    if request.method == "POST":
        if remove_note(notes, title): 
            save_notes(notes)
        return redirect("/notes")
      

@app.route("/note/edit/<title>", methods=["GET", "POST"])
def edit_notes(title):
    global notes
    if request.method == "POST":
        new_title = request.form.get("new_title")
        new_description = request.form.get("new_description")
        new_author = request.form.get("new_author")
        new_labels = request.form.get("new_labels")
        new_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        
        success = edit_note(notes, title, new_title=new_title, new_description=new_description, new_author=new_author, new_labels=new_labels, new_time=new_time)
        if success:
            if title in notes:
                save_notes(notes)
            return redirect(url_for('view_notes', _anchor=new_title))
        else:
            return redirect("/notes")
    else:
        note = notes.get(title)
        if note:
       
            if note.get('is_public'):
                return render_template("edit.html", note=note)
           
            elif session.get('username') == note.get('author'):
                return render_template("edit.html", note=note)
            else:
                return "You are not authorized to edit this note"
        else:
            return "Note not found", 404
    
@app.route("/logout")
def logout():
    global logged_in, username
    session.pop('username', None) 
    logged_in = False
    username = ""
    return redirect("/") 

if __name__ == "__main__":
    app.run(debug=True)
