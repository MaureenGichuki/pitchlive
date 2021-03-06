from . import db
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager
from datetime import datetime

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class User(UserMixin,db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(2000))
    email = db.Column(db.String(2000),unique = True,index = True)
    role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))
    pass_secure = db.Column(db.String(2000))
    bio = db.Column(db.String(2000))
    profile_pic_path = db.Column(db.String())
    pitches=db.relationship('Pitch',backref = 'user',lazy="dynamic")
    

    
    @property
    def password(self):
        raise AttributeError('Cannot view password')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)


    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)

   
    def __repr__(self):
        return f'User {self.username}'

class Role(db.Model):
    __tablename__='roles'

    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(255))
    users = db.relationship('User',backref = 'role',lazy="dynamic")

    def __repr__(self):
        return f'Role {self.name}'


class Pitch(db.Model):
    __tablename__='pitches'
    id = db.Column(db.Integer,primary_key = True)
    title = db.Column(db.String(200))
    pitch = db.Column(db.String(1000))
    posted = db.Column(db.DateTime,default=datetime.utcnow)
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))
    upvote = db.relationship('Upvote',backref = 'user',lazy="dynamic")
    downvote = db.relationship('Downvote',backref = 'user',lazy="dynamic")

    def save_pitch(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_pitches(cls,id):
        pitches = Pitch.query.order_by(Pitch.posted.desc())
        return pitches

    def __repr__(self):
        return f'Pitch {self.pitch}'

class Comment(db.Model):

    __tablename__='comments'
    id = db.Column(db.Integer,primary_key = True)
    comment = db.Column(db.String(240))
    posted = db.Column(db.DateTime,default=datetime.utcnow)
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))
    pitch_id=db.Column(db.Integer,db.ForeignKey("pitches.id"))

 
    def save_comment(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def get_comments(cls,id):
            comments = Comment.query.filter_by(pitch_id=id).all()
            return comments
    
    def __repr__(self):
        return f'Comment {self.comment}'

class Upvote(db.Model):

    __tablename__ = 'upvotes'
    id = db.Column(db.Integer,primary_key = True)
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))
    pitch_id=db.Column(db.Integer,db.ForeignKey("pitches.id"))


    def save_upvote(self):
        db.session.add(self)
        db.session.commit()

    def add_upvotes(cls,id):
        upvote_pitch = Upvote(pitch_id=id)
        upvote_pitch.save_upvotes()

    @classmethod
    def get_upvotes(cls,id):
            upvotes = Upvote.query.filter_by(pitch_id=id).all()
            return upvotes

    def __repr__(self):
        return f'Upvote {self.user_id}:{self.pitch_id}'

class Downvote(db.Model):

    __tablename__ = 'downpvotes'
    id = db.Column(db.Integer,primary_key = True)
    user_id = db.Column(db.Integer,db.ForeignKey("users.id"))
    pitch_id=db.Column(db.Integer,db.ForeignKey("pitches.id"))


    def save_downvote(self):
        db.session.add(self)
        db.session.commit()

    def add_downvotes(cls,id):
        upvote_pitch = Downvote( pitch_id=id)
        upvote_pitch.save_upvotes()

    @classmethod
    def get_downvotes(cls,id):
            downvotes = Downvote.query.filter_by(pitch_id=id).all()
            return downvotes

    def __repr__(self):
            return f'Upvote {self.user_id}:{self.pitch_id}'



    
    