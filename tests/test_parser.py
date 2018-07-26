""" Unit tests for Parser class """

import pytest

from pybot_app.parser import Parser

def test_clean_sentence():
    """ 
    Test the entire method. 
    Must return the last word of the sentence. 
    """
    sentence = Parser("Bonjour, savez-vous où se situe ma maison ?")
    assert sentence.clean_sentence() == "maison"

def test_clean_sentence_without_stop_words():
    """
    Test if the stop words treatment is not killing the main method
    """
    sentence = Parser("Pybot aide utilisateur")
    assert sentence.clean_sentence() == "utilisateur"

def test_clean_sentence_str_lower():
    """
    Test if the sentence is changed to lower case
    """
    sentence = Parser("Utilisateur aime PyBot")
    assert sentence.clean_sentence() == "pybot"

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

#"y-a-t'il" case
# def test_clean_sentence_multiple_punctuation():
#     sentence = Parser("y-a-t'il")

#     with pytest.raises(ValueError):
#         sentence.clean_sentence()