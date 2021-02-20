from datetime import datetime
from flask import render_template, session, redirect, url_for, flash, request
from .forms import NameForm
from .. import db
from . import main
from . import forms, error 
from .. import email
from ..models import Members, Admins, Post



# Main home Page
@main.route('/', methods=['GET', 'POST'])
def index():
  print('Admins TABLE: ')
  print(Admins.query.all())
  print('Post TABLE: ')
  print(Post.query.all())
  form = NameForm()
  if form.validate_on_submit():
    first_name = Members.query.filter_by(first_name=form.first_name.data).first()
    if first_name is None:
      member = Members(first_name=form.first_name.data,last_name=form.last_name.data,email=form.email.data)
      print(Members.query.all()) #Show an updated database
      send_email(form.email.data,'New User','/mail/new_user')
    # Dont commit to the database if the email alreay exist in the database  
      if Members.query.filter_by(email=form.email.data).count() < 1:
        db.session.add(member)
        db.session.commit()
        session['known'] = False
    else:
      session['known'] = True
      print(Members.query.all()) #Show an updated database
    session['name'] = form.first_name.datas
    #reset for the form 
    form.first_name.data = ''
    form.last_name.data = ''
    form.email.data = ''
    return redirect(url_for('main.index')) 
  posts = Post.query.order_by(Post.timestamp.desc()).all()
  return render_template('home.html', name=session.get('name'),form=form,current_time=datetime.utcnow(), known=session.get('known', False), posts=posts)

