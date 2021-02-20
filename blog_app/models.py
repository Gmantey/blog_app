from flask_login import UserMixin, AnonymousUserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from . import db, login_manager


#DATA Admins Posts
class Admins(UserMixin,db.Model):
  __tablename__ = 'Admins'
  __table_args__ = {'extend_existing': True}

  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(64), index=True)
  password = db.Column(db.String(64))
  password_hash = db.Column(db.String(128))
  # Relationships
  posts = db.relationship('Post', backref='RA_Post')
  residents = db.relationship('Members', backref='RA')

  def __repr__(self):
    return '<Admins %r>' % self.username
  
  @property 
  def password(self): 
    raise AttributeError('password is not a readable attribute')
  
  @password.setter
  def password(self, password):
    self.password_hash = generate_password_hash(password)
  
  def verify_password(self, password):
    return check_password_hash(self.password_hash, password)

#DATA BASE Tables 
class Members(db.Model): 
  __tablename__ = 'Members'
  __table_args__ = {'extend_existing': True}
          
  id = db.Column(db.Integer, primary_key=True)
  first_name = db.Column(db.String(64), index=True)
  last_name = db.Column(db.String(64), index=True)
  email = db.Column(db.String(64), unique=True, index=True)
  admin_id = db.Column(db.Integer, db.ForeignKey('Admins.id')) #Foreign 
  
  def __repr__(self):
    return '<Members %r>' % self.first_name

#DATA BASE Posts
class Post(db.Model):
  __tablename__ = 'Post'
  __table_args__ = {'extend_existing': True}
  
  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.String(128))
  subheading = db.Column(db.String(128))
  description = db.Column((db.Text))
  timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
  post_name = db.Column(db.String(128))
  admin_id = db.Column(db.Integer, db.ForeignKey('Admins.id')) #Foreign 

  
  def __repr__(self):
    return '<Post %r>' % self.title

# User Loader function
@login_manager.user_loader
def load_user(user_id):
  return Admins.query.get(int(user_id))
