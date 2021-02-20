from flask import render_template, session, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required, current_user
from . import auth
from .. import db
from ..models import Admins
from .forms import LoginForm, MakePost
from ..email import send_email

#Login View function
@auth.route('/login', methods=['GET', 'POST'])
def login():
  form = LoginForm()
  if form.validate_on_submit():
    admin = Admins.query.filter_by(username=form.username.data).first()
    if admin is not None and admin.verify_password(form.password.data):
      login_user(admin, form.remember_me.data)
      next = request.args.get('next')
      if next is None or not next.startswith('/'):
        next = url_for('main.post')
      return redirect(next)
    flash('Invalid username or password.')
  return render_template('login.html', form=form)

#LogOUT View function
@auth.route('/logout')
@login_required
def logout():
  logout_user()
  flash('You have been logged out.')
  return redirect(url_for('main.index'))


# View funciton for protected Login
@auth.route('/posttostudents', methods=['GET', 'POST'])
@login_required
def post():
  form = MakePost()
  current_RA = current_user._get_current_object()
  if form.validate_on_submit():
    f = form.post.data
    filename = current_RA.username + '/' + secure_filename(f.filename) 
    f.save(os.path.join(os.path.abspath('static/images'), filename))
    p = Post(title=form.title.data, subheading=form.Subheading.data, description=form.Description.data, post_name=filename, RA_Post=current_RA)
    db.session.add(p)
    db.session.commit()
    # Send A notification to all the residents in the RA's list VIA EMAIL
    email_list = []
    for resident in current_RA.residents:
      email_list.append(resident.email)
    print('RA ' + current_RA.username  + ' Email List: ')
    print(email_list)
    send_email(email_list,form.title.data,'/mail/new_user')
    return redirect(url_for('main.index'))
  return render_template('post.html', form=form) 
