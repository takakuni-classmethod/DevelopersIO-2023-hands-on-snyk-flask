#### Database Constructs
import sqlalchemy
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    email = db.Column(db.String(128), unique=True, nullable=False)
    password = db.Column(db.String(64), nullable=False)

def bootstrap(app):
    app.app_context().push()
    db.create_all()
    try:
        db.session.add(Users(username="badguy", email="badguy@example.com", password="badguy"))
        db.session.add(Users(username="john", email="john@example.com", password="john"))
        db.session.commit()
    except sqlalchemy.exc.IntegrityError:
        print("Database already pre-loaded...")

def get_user_by_password(username, password):
    return Users.query.filter_by(username=username, password=password).first()

def get_user(username):
    return Users.query.filter_by(username=username).first()