""" Mock test for Wiki class """

import requests

from pybot_app.wiki import Wiki

# Mock a Wiki Media API response
FAKE_WIKI_RESPONSE = [
    "wiki element",
    [
        "Wiki Title"
    ],
    [
        "Wiki short description"
    ],
    [
        "https://fake-wiki.com"
    ]
]

def fake_requests_get(*args, **kwargs):
    """ Function who is a mock of Requests.get() """
    return FakeResponseFromRequestsGet()

class FakeResponseFromRequestsGet:
    """ Class who is a mock of the Response object given by Requests.get() with a json method """
    def json(self):
        """ Return the fake response """
        return FAKE_WIKI_RESPONSE

def test_wiki(monkeypatch):
    """ Test if the Wiki constructor is not crashing """
    # Monkeypatch replace requests.get() by our fake_responses_get mock
    monkeypatch.setattr(requests, 'get', fake_requests_get)
    assert Wiki("test")

def test_wiki_entity(monkeypatch):
    """ Test the wiki entity return """
    monkeypatch.setattr(requests, 'get', fake_requests_get)
    assert Wiki("test").entity == "Wiki Title"

def test_wiki_details(monkeypatch):
    """ Test the wiki details return """
    monkeypatch.setattr(requests, 'get', fake_requests_get)
    assert Wiki("test").details == "Wiki short description"

def test_wiki_link(monkeypatch):
    """ Test the wiki link return """
    monkeypatch.setattr(requests, 'get', fake_requests_get)
    assert Wiki("test").wiki_link == "https://fake-wiki.com"
