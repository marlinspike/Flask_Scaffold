from flask_sqlalchemy import SQLAlchemy
from __init__ import db
from datetime import datetime

class Prefs(db.Model):
    
    def __str__(self):
        return f"Pref: {self.pref}, Value: {self.value}, Default: {self.default}, Created: {self.date_created} "

    def __repr__(self):
        return f"<User> {self}"

    id = db.Column(db.Integer, primary_key=True)
    pref = db.Column(db.String(50))
    value = db.Column(db.String(50))
    default = db.Column(db.String(50))
    date_created = db.Column(db.DateTime, default=datetime.now)
