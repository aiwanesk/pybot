""" Views function """
from flask import render_template, url_for, flash, redirect
from pybot_app import app
from pybot_app.form import AddressForm
from pybot_app.parser import Parser
from pybot_app.map import Map


@app.route('/', methods=['GET', 'POST'])
def index():
    form = AddressForm()
    if form.validate_on_submit():
        # Initialize an object to parse the data sent in form
        client_ask = Parser(form.address.data)
        # Get the main address keyword
        address_keyword = client_ask.clean_sentence()
        # Call OSM API 
        address = Map(address_keyword)

        # Get address informations
        address_latitude = address.latitude
        address_longitude = address.longitude
        address_details = address.address_details

        flash('Votre demande : {}'.format(form.address.data))
        flash('Ma demande par la classe : ' + client_ask.clean_sentence())
        flash('Latitude : {}'.format(address_latitude))
        flash('Longitude : {}'.format(address_longitude))
        flash('Details : {}'.format(address_details))
        
        return redirect(url_for('index'))
        
    return render_template('index.html', form=form)