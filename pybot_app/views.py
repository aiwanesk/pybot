""" Views function """
from flask import render_template, url_for
from pybot_app import app
from pybot_app.form import AddressForm


@app.route('/', methods=['GET', 'POST'])
def index():
    form = AddressForm()
    return render_template('index.html', form=form)