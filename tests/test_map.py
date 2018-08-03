""" Mock test for Map class """

import requests
from pytest import fixture
import json

from pybot_app.map import Map

paris_fake_response = """[
        {
            "lat": "49.8566101",
            "lon": "2.3514993",
            "address": {
                "city": "Paris",
                "county": "Paris",
                "state": "Île-de-France",
                "country": "France",
                "country_code": "fr"
            }
        }
    ]"""

@fixture(scope="function")
def mocked_request(monkeypatch):
    """ Mock an API OSM call to get address informations from a keyword """
    class MockedResult(object):

        def __init__(self, results):
            self.results = results

        def json(self):
            return json.loads(self.results)

    def mockreturn(request):
        return MockedResult(paris_fake_response)

    monkeypatch.setattr(requests, 'get', mockreturn)


def test_http_return(mocked_request):
    
    assert Map("paris")._get_map_informations() == paris_fake_response

def test_latitude(mocked_request):
    """ Test the latitude recovery """
    assert Map("paris").latitude == "49.8566101"

def test_longitude(mocked_request):
    """ Test the longitude recovery """
    assert Map("paris").longitude == "2.3514993"

def test_details(mocked_request):
    """ Test the address details recovery """
    assert Map("paris").details == {'city': 'Paris', 'county': 'Paris', 'state': 'Île-de-France', 'country': 'France', 'country_code': 'fr'}