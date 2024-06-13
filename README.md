# Project 4: The Final Project

Note Web App

## Description

Now that we've setup our basic command line interface, let's start working on the actual web application! This project has a lot more freedom for you! The base requirement is for you to add the web app functionality to the overarching project. Once you have this, I want you to pick at least **4** features from the list below to implement to your web app! In order to get credit, these features **must** work. By doing the required features correctly, you will get at least a 75 on this project. This project has a cap of 180 points <sup>[1]</sup>.

## Tech Stack

- Python 3 
- Flask 
- HTML
- CSS

## Setup 

- Install Flask
    - On Mac/Linux: run `pip3 install flask`
    - On Windows: un `pip install flask`
- Run the app using `python3 app.py` and visit [http://localhost:5000](http://localhost:5000). Flask will naturally use port 5000.

## Instructions

### Exploration

- Start by running the application and viewing the base website. This should open to a simple "My notes app" page with not much inside. 
- Navigate to the [/login](http://localhost:5000/login) or the [/signup](http://localhost:5000/signup) pages to get logged in or signed up. These will also be blank outside of a simple form. You will implement the post request (data processing) for these forms. Lastly, check out the [/notes](http://localhost:5000/notes) page to see the list of notes. Clicking on these will direct you to a simple page with the note title and a back button. 
- Coming back to the code, notice that the functions from project 3 have been mostly moved into the `util.py` file. This is intentional. This allows us to still run the `command-line.py` file. This file is effectively project 3 and allows us to see how our code can serve multiple systems.
- Now, look at the `app.py` file. This contains the starter code for the Flask server. Each function is a route for the backend to serve to the frontend. Notice how some of these functions contain the `methods=["POST"]` part. This ensures that the specific routes can also be used in forms. There are also `methods = ["GET", "POST"]`**? in the code. This ensures that some routes can also serve a webpage while also handling the data. Lastly, if a route doesn't include a `methods` argument, it means that the route only serves a webpages - implying only a GET request can be used.**
- Now, open up the `templates` folder. All of the core web pages are being rendered from html files from the `templates` folder. Look over the templates briefly. Notice that each page contains a &lt;style&gt; tag and a &lt;link&gt; tag. The style tag itself allows for you to create styles for that specific page, while the link tag imports styles from the `static/styles/styles.css` file. 
- Lastly, check out the `static/styles/styles.css` file. This contains any global CSS that you want to include on all pages without having to rewrite the same styles in each style tag.

### Getting Started

- You may start with either the python server code: flask portion, or by designing the web pages: design portion.

#### Python Server Code: Flask portion

- The python server code requires you to focus on the `app.py` file, implementing most of the `POST` requests. These require you to process the data coming from the request.form. You will have to consider the different types of data coming in. It may help you to print out the data in the `request.form` variables.
- Read through the various TODOs written in the code.

- **Signup page**: In the POST request, the form data should be the `username` and the `password`. Pass this data into the `signup` function. If the `signup` function succeeded, it should return True. If it returns True, take the username of the inputted user and set that into the global `username` variable, then set the global `logged_in` variable to `True`. This will ensure the program knows the user is logged in. If the signup succeeded, call `save_users` with the `users` variable. This will ensure our new user is kept track of. Lastly, `return redirect("/")` to send the user back to the main page. If the sign up failed, return "Failed signup" instead.
- **Login page**: This will follow the same setup as the signup function, but use the `login` utility function. Additionally, this function does not need to save the users as no new users have been created here. Additionally, if the login failed, return "Failed login". Most of the implementation of the login path follows the same setup as the signup path.
- **New note**: This POST request should take in the information from a form. This form should include the `title`, `description`, and the `labels`. Take each value from the form and pass it into the `add_note` function, along with the original dictionary of notes. Once the new note has been created, call `save_notes` as we need to update our file containing all of our notes. Lastly, redirect the user to the notes path if it succeeded. If it failed to create a new note, return "Failed to save note" and don't call the `save_notes` function.
- **Get note**: This should simply call the `view_note` function and pass the note into the template. Replace the `note = None` with `note=view_note(notes, title)`.
- **Remove note**: In remove note, take the title from the form, pass it into the `remove_note` function. If it succeeds, call `save_notes` to update our file with the removed note. If it fails, return "Failed to remove note". You will have to think of where this POST request is called in your front end.

#### HTML Design: Design portion

- Go through the HTML and update the interfaces. Some of them require you to create the forms - such as the notes page requiring an input form somewhere. All of these pages require work to design them, as otherwise, the pages continue to be plain and boring.

- **Index**: Add a Navigation bar at the top to direct users to different paths in the web app. Add your own styles. You can even include an area to show the notes if you please.
- **Login/Signup**: Add a Navigation bar at the top to direct users to different paths in the web app. Add your own styles.
- **Notes**: Add a Navigation bar at the top to direct users to different paths in the web app. Add your own styles. You can also add aspects to the link to each note. Additionally, if you want to try, you may be able to have the user delete a note from this page. Add an input for the user to create new notes from this page.
- **Note**: Add more details to the note itself. Allow the user to delete the note here. Add a navigation bar to the top to direct users to different paths in the web app. Add your own styles. If you want to take the challenge of editing a note and processing that, you can too. This would be a good place to do that.

## Required Features

- Use Flask to create a web app. 
- Users must be able to log into the system 
- Users must be able to create a new account
- Users must be able to create, view, update, and delete their own notes 
- Create HTML templates and store them into the `/templates/` folder. These will be used for the interface instead of long strings containing HTML code.

## Possible Features 

Check off which features you implement.

- [x] Edit Notes: Allow the user to edit a note (+5)
- [x] Web App Design: Create a well designed website: (+5)
- [ ] Add an API: Add an API of your choosing: (+5)
- [ ] Fine-tuned search: Implement a Search Algorithm: (+5)
- [ ] Filter notes: Allow the user to filter notes by labels (+5)
- [x] Sort notes: Sort the notes by some sortable value. (+5)
- [ ] Use classes and objects to represent the Notes: Convert the system to use Classes and Objects instead of only functions and dictionaries (+10)
- [ ] Allow the user to download their data (+10)
- [ ] Allow the user to customize settings around the app (+10)
- [ ] Notes lists that contain different kinds of notes (+10)
- [ ] Statistics for the user (+15)
- [ ] Different types of notes with different values being stored (+15)
- [ ] Note categories (+10)
- [x] Note Timeline (+20)
- [x] Note Privacy: A note can be public or private. If a note is public, other users can view it. If a note is private, only the author can view the note.  (+15)
- [ ] Integrate a Todo List program into this project (+5)
- [ ] Provide potential prompts for the user to consider when creating notes (+5)
- [ ] Add command line arguments to change the behavior of the program when the program is executed (+5)
- [ ] Note encryption (+10)
- [ ] Forgot Password functionality; allow the user to reset their password (+10)
- [ ] Add a Graphical User Interface with PySimpleGUI or TKinter (+10)
- [ ] Session tracking using Cookies <sup>[2]</sup> (+20)
- [ ] Tokenizing users with jwt <sup>[2]</sup> (+25)
- [ ] Deploy this live on Render **(jwt must be done)** <sup>[2], [3]</sup> (+20)
- [ ] Pitch your own! Send me an email with what features you want to implement and we can set up a meeting discussing them, along with how the points can be given based on the features.

## Footnotes 

- [1] I know adding up all of the extra credit comes out to more than 180. This is to make sure that your time is well spent and you're not trying to implement everything. I'd rather you take the time to implement features with quality, over having more quantity and none of them work.
- [2] Come see me in my Office Hours and I'll explain what these are doing.
- [3] JWT has to be done first due to security issues. Also, come see me in my Office Hours if you want to know more and I'll explain why.

