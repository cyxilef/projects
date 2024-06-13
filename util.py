from json import load, dumps, JSONDecodeError

def range_input(prompt, min, max):
    while True:
        try:
            user = int(input(prompt))
            if user < min or user > max:
                    raise TypeError
            return user 
        except ValueError:
            print("Not a number.")
        except TypeError:
            print(f"Out of range, values must be between {min} and {max}")

def encrypt(password, shift):
    encrypted = ""
    for char in password:
        encrypted += chr(ord(char) + shift)
    return encrypted

def load_users():
    try: 
        with open("users.json", 'r') as f:
            try:
                return load(f)
            except JSONDecodeError:
                return {}
    except FileNotFoundError:
        print("No users found")
        return {}

def load_notes():
    try: 
        with open('notes.json', 'r') as f:
            try: 
                return load(f)
            except JSONDecodeError:
                return {}
    except FileNotFoundError:
        print("No notes found")
        return {}

def save_users(users):
    with open("users.json", 'w') as f:
        f.write(dumps(users))

def save_notes(notes):
    with open('notes.json', 'w') as f:
        f.write(dumps(notes))


def add_note(notes, title, description, author, labels, timestamp, is_public=True, is_private=True):
    notes[title] = {
        "title": title,
        "description": description,
        "author": author,
        "labels": labels,
        "timestamp": timestamp,
        "is_public": is_public,
        "is_private": is_private
    }
    return notes[title]

def remove_note(notes, title):
    if title not in list(notes.keys()):
        return False
    notes.pop(title)
    return True

def view_note(notes, title):
    if title not in list(notes.keys()):
        return None
    return notes.get(title)

def signup(users, username, password):
    for user in users:
        if user == username: 
            return False 
    users[username] = encrypt(password, 2)
    print("User successfully created!")
    return True 

def login(users, username, password):
    for stored_user in users:
        stored_username = stored_user
        stored_password = users[stored_user]
        if(stored_username == username):
            if(encrypt(password, 2) == stored_password):
                print("Successfully logged in!")
                return True
    return False


def edit_note(notes, title, new_title=None, new_description=None, new_author=None, new_labels=None, new_time=None):
    if title not in notes:
        return False
    note = notes[title]
    if new_title is not None:
        if new_title != title and new_title in notes:
            return False
        note['title'] = new_title
    if new_description:
        note['description'] = new_description
    if new_author:
        note['author'] = new_author
    if new_labels:
        note['labels'] = new_labels
    if new_time:
        note['timestamp'] = new_time 
    return True
