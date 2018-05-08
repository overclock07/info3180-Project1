from app import db
from datetime import datetime

class userprofile(db.Model):
    userid = db.Column('userid', db.Integer, primary_key=True)
    firstname = db.Column(db.String(80))
    lastname = db.Column(db.String(80))
    gender = db.Column(db.String(80))
    email = db.Column(db.String(80))
    location = db.Column(db.String(80))
    biography = db.Column(db.String(80))
    image = db.Column(db.String(80))
    created_on = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __init__(self, firstname, lastname, gender, email, location, biography, image):
        self.firstname = firstname
        self.lastname = lastname
        self.gender = gender
        self.email = email
        self.location = location
        self.biography = biography
        self.image = image
      

    def __repr__(self):
        return '<UserProfile %r>' % self.username
