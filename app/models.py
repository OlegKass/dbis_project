from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from datetime import datetime


db = SQLAlchemy(app)
migrate = Migrate(app, db)


class User(db.Model):

	uid = db.Column(db.Integer, primary_key=True)
	login = db.Column(db.String(128), nullable=False)
	password = db.Column(db.String(64), nullable=False)
	email = db.Column(db.String(128), nullable=False)
	name = db.Column(db.String(128), nullable=False)
    cookie = db.Column(db.String(128), nullable=False)
    type = db.Column(db.String(128), nullable=False)
    photo = db.Column(db.String(128), nullable=False)

	def __repr__(self):
		return f'<User {self.uid}>'


class Student(db.Model):
    Student_id = db.Column(db.Integer, primary_key=True)
    Group = db.Column(db.String(128), nullable=False)
    Department = db.Column(db.String(128), nullable=False)

class Professor(db.Model):
    Professor_id = db.Column(db.Integer, primary_key=True)
    Department = db.Column(db.String(128), nullable=False)

class Channel(db.Model):
    uid = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(128), nullable=False)
    photo = db.Column(db.Integer, nullable=False)

class Post(db.Model):
	Post_id = db.Column(db.Integer, primary_key=True)
    Channel_id = db.Column(db.Integer, nullable=False)
    Text = db.Column(db.String(128), nullable=False)
    Attachments = db.Column(db.Integer, nullable=False)
    Author_id = db.Column(db.Integer, nullable=False)


class User_Channel(db.Model):
    User_id = db.Column(db.Integer, primary_key=True)
    Channel_id = db.Column(db.Integer, primary_key=True)

class User_types(db.Model):
    UserType_id = db.Column(db.Integer, primary_key=True)
    Type = db.Column(db.String(128), nullable=False)

class Attachment(db.Model):
    uid = db.Column(db.Integer, primary_key=True)
    path = db.Column(db.String(128), nullable=False)

class Comment(db.Model):
	comid = db.Column(db.Integer, primary_key=True)
	text = db.Column(db.Text, nullable=False)
	author = db.Column(db.Integer, db.ForeignKey(User.uid, ondelete="CASCADE"), nullable=False)
	date = db.Column(db.DateTime, default=datetime.now)
	# ...

	def __repr__(self):
		return f'<Comment {self.comid}>'
