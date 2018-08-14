""" Unit tests for Parser class """

import pytest

from pybot_app.parser import Parser

def test_clean_sentence():
    """
    Test the entire method.
    Must return the last word of the sentence.
    """
    sentence = Parser("Bonjour, savez-vous où se situe la Tour Eiffel ?")
    assert sentence.clean_sentence() == "tour eiffel"

def test_clean_sentence_without_stop_words():
    """
    Test if the stop words treatment is not killing the main method
    """
    sentence = Parser("Ordinateurs soutiennent utilisateur")
    assert sentence.clean_sentence() == "ordinateurs soutiennent utilisateur"

def test_clean_sentence_str_lower():
    """
    Test if the sentence is changed to lower case
    """
    sentence = Parser("Je veux aller à Paris")
    assert sentence.clean_sentence() == "paris"

def test_clean_sentence_return_str():
    """
    Test if the sentence doesn't contain words
    """
    sentence = Parser("! , . / =")

    with pytest.raises(ValueError):
        sentence.clean_sentence()

def test_clean_sentence_send_no_value():
    """
    Test if no sentence is send
    """
    sentence = Parser("")

    with pytest.raises(ValueError):
        sentence.clean_sentence()

def test_clean_sentence_returns_no_data():
    """
    Test if no parser returns no data
    """
    sentence = Parser("Bonjour !")

    with pytest.raises(ValueError):
        sentence.clean_sentence()

def test_clean_sentence_word_with_punctuation():
    """
    Test if word with punctation is correctly processed
    """
    sentence = Parser("Salut, je veux découvrir Paris!")
    assert sentence.clean_sentence() == "paris"
