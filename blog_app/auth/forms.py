from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, FileField, BooleanField , PasswordField
from wtforms.validators import DataRequired, Length


# Admin Log in Form
class LoginForm(FlaskForm):
  username = StringField('Username', validators=[DataRequired(), Length(1, 64)])
  password = PasswordField('Password', validators=[DataRequired()])
  remember_me = BooleanField('Keep me logged in')
  submit = SubmitField('Log In')

# Make a Post
class MakePost(FlaskForm):
  title = StringField('Title', validators=[DataRequired(), Length(1,128)])
  Description = TextAreaField('Description', validators=[DataRequired(), Length(1,128)])
  Subheading = StringField('Sub Heading', validators=[DataRequired(), Length(1,128)])
  post = FileField('Upload File', validators=[DataRequired()])
  submit = SubmitField('Post')