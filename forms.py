from flask_wtf import FlaskForm
from wtforms.fields import *
from wtforms.validators import Required

class LocationForm(FlaskForm):
    city = TextField('Your City (in English)', validators=[Required()])
    weatherbit_api_key = StringField('Your personal WeatherBit API Key (optional)')
    submit = SubmitField('Check weather')
