import sys
from flask import Flask
from flask import render_template
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir) 
from models import user
from __init__ import db
from __init__ import app
from models.user import User


@app.route('/create/<first>/<last>/<email>')
def index(first, last, email):
    u = User(first = first, last = last, email = email)
    db.session.add(u)
    db.session.commit()

    return "Added new user!"

@app.route('/delete/<first>')
def delete(first):
    u:User = User.query.filter_by(first = first).first()
    username = u.first
    db.session.delete(u)
    db.session.commit()
    return f"Deleted User: {username}"

@app.route('/read/<first>')
def find(first):
    u:User = User.query.filter_by(first = first).first()
    return render_template('user.html', u=u)
    #return f"User found: {u}"


@app.route('/update/<first>/<new_first>')
def update(first, new_first):
    u:User = User.query.filter_by(first = first).first()
    u.first = new_first
    db.session.merge(u)
    db.session.commit()
    u:User = User.query.filter_by(first = new_first).first()
    username = u.first
    return f"Updated User: {username}"

app.run()

