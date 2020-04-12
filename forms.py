from flask_wtf import FlaskForm
from wtforms.fields import *
from wtforms.validators import Required

class LocationForm(FlaskForm):
    location = TextField('Your location', validators=[Required()])
    submit = SubmitField('Check weather')
