## Flask SQLAlchemy Basic CRUD
This is a scaffold app for use by my **SharpKidsCode** students to build basic CRUD using Flask and SQLAlchemy

## Requirements
Please make sure you have Python 3 installed.

## Pyenv
Remember to cerate a Virtual Environment to run python. It's a good practice for any app you're building, so that you can isolate dependencies by app, and build a requirements file unique to each app's unique needs.

It's customary to call that virtual environment 'venv', and here's how you'd do it from the root of your app's folder:
`python -m venv venv`

Then you switch to using the python installed in your virtual environment:
`source ./venv/bin/activate`

To deactivate your virtual environment (and switch back to global python):
`deactivate`

## First steps
Install the required dependencies. You can do this via the following command when you're at the root of the application in your Terminal:

`pip install -r requirements.txt`

## Creating the database
While the code already contains a complete DB, you can re-create it anytime. Run Python in the root directory of the app, and then run:
`from app import db`
`db.create_all()`
`quit()`

That should create an **app.sqlite3** file in the root directory of your app with the models for Users and Prefs created.

## Running the app
`python app.py`

## Where to go from here
For students following along, we'll have regular updates on progress posted in regular class repository.