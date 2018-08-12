""" Unit tests for BotAnswer class """

from pybot_app.bot_answer import BotAnswer

def test_botanswer():
    """ Test if BotAnswer constructor is good """
    assert BotAnswer()

def test_random_address_answer():
    """ Test if random_address_answer returns an element of address_answer possibility """
    assert BotAnswer().random_address_answer in BotAnswer()._answer["address_answer"]

def test_random_wiki_answer():
    """ Test if random_wiki_answer returns an element of wiki_answer possibility """
    assert BotAnswer().random_wiki_answer in BotAnswer()._answer["wiki_answer"]

def test_random_error_answer():
    """ Test if random_error_answer returns an element of error possibility """
    assert BotAnswer().random_error_answer in BotAnswer()._answer["error_answer"]
