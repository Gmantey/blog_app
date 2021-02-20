from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length


#### FORMS ####

# Sign up Form
class NameForm(FlaskForm):
  first_name = StringField('First Name', validators=[DataRequired()])
  last_name = StringField('Last Name', validators=[DataRequired()])
  email = StringField('Email', validators=[DataRequired()])
  submit = SubmitField('Submit')

