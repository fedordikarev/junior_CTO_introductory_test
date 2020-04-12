#!/usr/bin/env python

from flask import Flask, render_template, flash, redirect, url_for, escape
# from flask_appconfig import AppConfig
from flask_bootstrap import Bootstrap

from forms import LocationForm

import os


app = Flask(__name__)
# AppConfig(app)
Bootstrap(app)

SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/location', methods=('GET', 'POST'))
def location():
    form = LocationForm()

    weather = dict()
    if form.validate_on_submit():
        flash('Hello, {}. You have successfully signed up'
              .format(escape(form.location.data)))
        weather['city'] = form.location.data
        weather['temperature'] = "36.6"
        # return redirect(url_for('.location'))

    return render_template('location.html', form=form, weather=weather)

if __name__ == '__main__':
    app.run()
