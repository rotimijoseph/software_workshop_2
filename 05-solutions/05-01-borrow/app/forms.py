from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, DateField, TextAreaField, DecimalField
from wtforms.validators import DataRequired, Length, EqualTo, ValidationError
from datetime import datetime, timedelta

class RegistrationForm(FlaskForm): 
	username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
	email = StringField('Email', validators=[DataRequired()])
	dob = DateField('Date of Birth', format='%Y-%m-%d', validators=[DataRequired()])
	phone = StringField('Phone Number', validators=[DataRequired(), Length(max=11)])
	address = TextAreaField('Address', validators=[DataRequired(), Length(max=200)])
	height = DecimalField('Height (cm)', validators=[DataRequired()])
	weight = DecimalField('Weight (kgs)', validators=[DataRequired()])
	password = PasswordField('Password', validators=[DataRequired()])
	confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
	submit = SubmitField('Sign Up')


	def validate_dob(self, dob):
          today = datetime.now().date()
          min_age_date = today - timedelta(days=18*365)
          max_birth_date = today - timedelta(days=365*120)
          if self.dob.data > min_age_date or self.dob.data < max_birth_date or self.dob.data > today:
            return False
          return True

class BorrowForm(FlaskForm):
    student_id = StringField('Student ID', validators=[DataRequired()])
    device_id = StringField('Device ID', validators=[DataRequired()])
    submit = SubmitField('Borrow')
