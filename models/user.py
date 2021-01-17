from flask_sqlalchemy import SQLAlchemy
from __init__ import db
from datetime import datetime

class User(db.Model):
    
    def __str__(self):
        return f"First: {self.first}, Last: {self.last}, Email: {self.email}, Created: {self.date_created} "

    def __repr__(self):
        return f"<User> {self}"

    id = db.Column(db.Integer, primary_key=True)
    first = db.Column(db.String(50))
    last = db.Column(db.String(50))
    email = db.Column(db.String(100))
    date_created = db.Column(db.DateTime, default=datetime.now)
    prefs = db.relationship('Pref', backref='user') #Allows you to navigate from Pref -> User
