from flask import Flask, redirect, render_template, url_for, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os,sys,inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0,parentdir) 
from models import user
from __init__ import db, app
from models.user import User


#Add user by QueryString
@app.route('/create/<first>/<last>/<email>', methods = ['GET'])
def index(first, last, email):
    u = User(first = first, last = last, email = email)
    db.session.add(u)
    db.session.commit()
    return "Added new user!"

#Create User by Form
@app.route('/create_user', methods = ['GET', 'POST'])
def create_user():
    if request.method == 'GET':
        return render_template("user/user_create.html")
    else:
        first = request.values.get("first")
        last = request.values.get("last")
        email = request.values.get("email")
        u = User(first = first, last = last, email = email)
        db.session.add(u)
        db.session.commit()
        return render_template("user/user.html", u = u)


#Delete User
@app.route('/delete_user/<user_id>')
def delete_user(user_id):
    u:User = User.query.filter_by(id = user_id).first()
    db.session.delete(u)
    db.session.commit()
    return redirect(url_for('list'))

#Get User by First Name
@app.route('/read/<first>', methods = ['GET'])
def find(first):
    u:User = User.query.filter_by(first = first).first()
    return render_template('user/user.html', u=u)
    #return f"User found: {u}"

#List users
@app.route('/list')
def list():
    users = User.query.all()
    return render_template('user/user_list.html', users=users)

@app.route('/update_user/<user_id>', methods = ['GET', 'POST'])
def update_user(user_id):
    if request.method == 'GET':
        u:User = User.query.filter_by(id = user_id).first()
        return render_template("user/user_update.html", u=u)
    else:
        id = request.values.get("user_id")
        first = request.values.get("first")
        last = request.values.get("last")
        email = request.values.get("email")
        u:User = User.query.filter_by(id = id).first()
        u.first = first
        u.last = last
        u.email = email
        db.session.merge(u)
        db.session.commit()
        return redirect(url_for('list'))

#Update User by QueryString
@app.route('/update/<first>/<new_first>', methods = ['GET', 'POST'])
def update(first, new_first):
    u:User = User.query.filter_by(first = first).first()
    u.first = new_first
    db.session.merge(u)
    db.session.commit()
    u:User = User.query.filter_by(first = new_first).first()
    username = u.first
    return f"Updated User: {username}"

app.run(debug=True)

