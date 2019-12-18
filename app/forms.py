from app.models import *
from app.account import *
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField, SelectField, IntegerField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo, Length, Optional

class LoginForm(FlaskForm):
	username = StringField('Username', validators=[DataRequired()])
	password = PasswordField('Password', validators=[DataRequired()])
	remember_me = BooleanField('Remember Me')
	submit = SubmitField('Sign In')


class RegistrationForm(FlaskForm):
	username = StringField('Username *', validators=[DataRequired()])
	email = StringField('Email *', validators=[DataRequired(), Email()])
	group_id = IntegerField('Site ID', default=createDefaultGroup(), validators=[Optional()])
	password = PasswordField('Password *', validators=[DataRequired()])
	password_repeat = PasswordField('Repeat Password *', validators=[DataRequired(), EqualTo('password', message='Passwords must match.')])
	submit = SubmitField('Register')

	def validate_username(self, username):
		user = User.query.filter_by(username=username.data).first()
		if user is not None:
			raise ValidationError('Please use a different username.')

	def validate_email(self, email):
		user = User.query.filter_by(email=email.data).first()
		if user is not None:
			raise ValidationError('Please use a different email address.')

	def validate_group_id(self, gid):
		group = Group.query.filter_by(id=gid.data).first()
		if not group:
			raise ValidationError('Sorry! This group does not exist.')

class UpdateAccountForm(FlaskForm):
	username = StringField('Username', validators=[DataRequired()])
	email = StringField('Email', validators=[DataRequired(), Email()])
	submit = SubmitField('Update')

class UpdatePasswordForm(FlaskForm):
	password = PasswordField('Password', validators=[DataRequired()])
	password_repeat = PasswordField(
		'Repeat Password', validators=[DataRequired(), EqualTo('password')])
	submit = SubmitField('Update')
