""" Mock tests for Map() class """

import requests

from pybot_app.map import Map

FAKE_MAP_RESPONSE = [{
    "lat": "12.3456789",
    "lon": "9.87654321",
    "address": {
        "city": "Fake city",
        "state": "Fake state",
        "country": "Fake country",
        "country_code": "Fake country code"
    }
}]

class FakeResponseFromRequestsGet:
    """ Class who is a mock of the Response object given by Requests.get() with a json method """
    def json(self):
        """ Return the fake response """
        return FAKE_MAP_RESPONSE

def fake_requests_get(*args, **kwargs):
    """ Function who is a mock of Requests.get() """
    return FakeResponseFromRequestsGet()

def test_map(monkeypatch):
    """ Test if the Wiki constructor is not crashing """
    # Monkeypatch replace requests.get() by our fake_responses_get mock
    monkeypatch.setattr(requests, 'get', fake_requests_get)
    assert Map("test")

def test_latitude(monkeypatch):
    """ Test the latitude return """
    monkeypatch.setattr(requests, 'get', fake_requests_get)
    assert Map("test").latitude == "12.3456789"

def test_longitude(monkeypatch):
    """ Test the longitude return """
    monkeypatch.setattr(requests, 'get', fake_requests_get)
    assert Map("test").longitude == "9.87654321"

def test_details(monkeypatch):
    """ Test the address details return """
    monkeypatch.setattr(requests, 'get', fake_requests_get)
    assert Map("test").details == {
        "city": "Fake city",
        "state": "Fake state",
        "country": "Fake country",
        "country_code": "Fake country code"
    }
