""" Views function """
from flask import render_template, jsonify, request
from pybot_app import app
from pybot_app.form import AddressForm
from pybot_app.parser import Parser
from pybot_app.map import Map
from pybot_app.wiki import Wiki

@app.route('/ajax-osm', methods=['POST'])
def osm_ajax_request():
    result = request.form['address_request']

    # Initialize an object to parse the data sent in form
    client_ask = Parser(result)
    # Get the main address keyword
    address_keyword = client_ask.clean_sentence()
    # Call OSM API
    address = Map(address_keyword)
    # Call Wiki API
    address_informations = Wiki(address_keyword)
    print(address_informations.details)
    print(address_informations.wiki_link)

    # Get address informations
    try:
        address_latitude = address.latitude
        address_longitude = address.longitude
        address_details = address.details

        wiki_informations = address_informations.details
        wiki_link = address_informations.wiki_link

        return jsonify({'address': {
                        'latitude': address_latitude,
                        'longitude': address_longitude,
                        'details': address_details,
                        'wiki_informations': wiki_informations,
                        'wiki_link': wiki_link
                    }
                })
    except:
        return jsonify({'error' : "Cette adresse n'est pas répertoriée sur OpenStreetMap.org",
                        'status_code' : 404
        })


@app.route('/')
def index():
    # CSRF protection disabled as Ajax treatment
    form = AddressForm(csrf_enabled=False)
    return render_template('index.html', form=form)
