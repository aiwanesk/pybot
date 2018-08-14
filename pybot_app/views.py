""" Views function """

from flask import render_template, jsonify, request
from pybot_app import app
from pybot_app.form import AddressForm
from pybot_app.parser import Parser
from pybot_app.map import Map
from pybot_app.wiki import Wiki
from pybot_app.bot_answer import BotAnswer

@app.route('/ajax', methods=['POST'])
def osm_ajax_request():
    """
    Get the Ajax call
    Treat all requests (OSM + Wiki + bot answer)
    Return json responses
    """

    result = request.form['address_request']

    # Initialize an object to parse the data sent in form
    client_ask = Parser(result)
    # Get the main address keyword
    try:
        address_keyword = client_ask.clean_sentence()
    except ValueError:
        return jsonify({
            'answer_error': True
        })
    # Call OSM API
    address = Map(address_keyword)
    # Call Wiki API
    address_informations = Wiki(address_keyword)
    # Get a random answer
    pybot_answer = BotAnswer()

    # Get address informations
    try:
        address_latitude = address.latitude
        address_longitude = address.longitude
        address_details = address.details
        address_answer = pybot_answer.random_address_answer

        wiki_entity = address_informations.entity
        wiki_informations = address_informations.details
        wiki_link = address_informations.wiki_link
        wiki_answer = pybot_answer.random_wiki_answer

        return jsonify({'address': {
            'latitude': address_latitude,
            'longitude': address_longitude,
            'details': address_details,
            'address_answer': address_answer,
            'wiki_entity': wiki_entity,
            'wiki_informations': wiki_informations,
            'wiki_link': wiki_link,
            'wiki_answer': wiki_answer
            }
        })
    except:
        error_answer = pybot_answer.random_error_answer

        return jsonify({
            'error_answer': error_answer,
            'address_keyword': address_keyword
        })

@app.route('/')
def index():
    """ Display the index page with Flask form """

    # CSRF protection disabled as Ajax treatment
    form = AddressForm(csrf_enabled=False)
    return render_template('index.html', form=form)
