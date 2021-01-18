from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SECRET_KEY'] = "DFJH&#$^&DFJHAJHFHDGKJA@(18723816jh188fFA"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///app.sqlite3"
app.config['FLASK_ENV']="development"
app.config['SQLALCHEMY_ECHO']=True #Optionally show SQLAlchemy queries in the Debug log

db = SQLAlchemy(app)