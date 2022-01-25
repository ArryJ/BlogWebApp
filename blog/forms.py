from flask_wtf import FlaskForm
from wtforms import StringField,EmailField, PasswordField, SubmitField, IntegerField
from wtforms.validators import DataRequired, EqualTo, ValidationError, Regexp, NumberRange
from blog.models import User

class RegistrationForm(FlaskForm):
  first_name = StringField('First Name',validators=[DataRequired(),Regexp('^[[a-zA-Z0-9]{3,20}$',message='Your First Name should be between 3 and 20 characters long, and can only contain alphanumeric characters.')])
  email = EmailField('Email',validators=[DataRequired()])
  password = PasswordField('Password',validators=[DataRequired(),Regexp('^[[a-zA-Z0-9]{6,20}$',message='Your password contains invalid characters')])
  repeat_password = PasswordField('Repeat Password', validators=[ DataRequired(), EqualTo('password',message= 'Passwords do not match. Please try again')])
  submit = SubmitField('Register')

  def validate_email(self, email):
    user = User.query.filter_by(email=email.data).first()
    if user is not None:
      raise ValidationError('Email already exist. Please choose a different one.')



class LoginForm(FlaskForm):
  email = StringField('Username',validators=[DataRequired()])
  password = PasswordField('Password',validators=[DataRequired()])
  submit = SubmitField('Login')

class CommentForm(FlaskForm):
  content = StringField('Content', validators=[DataRequired()])
  submit = SubmitField('Add Comment')

class RatingForm(FlaskForm):
  stars = IntegerField('Stars', validators=[DataRequired(), NumberRange(min=0,max=5)])
  submit = SubmitField('Add Rating')
