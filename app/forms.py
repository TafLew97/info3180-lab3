from flask_wtf import FlaskForm
from wtforms import Form, TextField, TextAreaField, validators, SubmitField
from wtforms.validators import DataRequired, Email

class ContactForm(FlaskForm):
    name= TextField('Name', validators=[validators.DataRequired()])
    email= TextField('Email', validators=[validators.DataRequired()])
    subject= TextField('Subject', validators=[validators.DataRequired()])
    message= TextAreaField('Message', validators=[validators.DataRequired()])
    submit= SubmitField('Send', validators=[validators.DataRequired()])