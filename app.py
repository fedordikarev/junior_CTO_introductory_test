#!/usr/bin/env python

from flask import Flask, render_template, flash, redirect, url_for, escape
# from flask_appconfig import AppConfig
from flask_bootstrap import Bootstrap
import requests

from forms import LocationForm

import os


app = Flask(__name__)
# AppConfig(app)
Bootstrap(app)

SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY
app.config['WEATHER_KEY'] = os.getenv('WeatherBit_API_Key')

@app.route('/')
def hello_world():
    return redirect(url_for('weather'))

@app.route('/weather', methods=('GET', 'POST'))
def weather():
    form = LocationForm()

    weather = dict()
    if form.validate_on_submit():
        return render_template(
            'weather.html', form=form,
            weather=get_weather(city=form.city.data, key=form.weatherbit_api_key.data),
            banners=get_rtb_banners(),
        )

    return render_template(
        'weather.html', form=form,
        weather=dict(),
        banners=get_rtb_banners(),
    )

def get_rtb_banners():
    return []

def get_weather(city='Moscow', country='RU', key=None, lang='ru'):
    if not key:
        key = app.config['WEATHER_KEY']

    base_url = 'https://api.weatherbit.io/v2.0/current'
    result = requests.get(
            base_url,
            headers={'Accept': 'application/json'},
            params={'city': city, 'country': country, 'key': key, 'lang': lang},
            )

    if result.status_code == 403:
        return {'err': 'Bad WetherBit API Key'}
    result.raise_for_status()
    data = result.json()['data'][0]
    return dict(
        temperatue="{} {} ºC".format(data.get("weather", {}).get("description"), data.get('temp')),
        wind="{} m/s {}".format(data.get('wind_spd'), data.get('wind_cdir')),
    )



if __name__ == '__main__':
    app.run()
