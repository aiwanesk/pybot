""" Parser class """

import string
from pybot_app.stopwordsfr import STOP_WORDS_FR

class Parser():
    """ Cut and clean a sentence to return the main keyword """

    def __init__(self, sentence):
        self.sentence = sentence

    def clean_sentence(self):
        """ 
        Clean the sentence passed in argument
        Return the main word of the sentence
        """

        if self.sentence:
            # Each string element (separated by a space) is an element of a new list 
            split_sentence = self.sentence.split(" ")
        else:
            raise ValueError("Sentence is empty")

        cleaned_sentence = []
        word_to_add = True
        # Main loop to clean the sentence
        for word in split_sentence:
            word = word.lower()

            # To delete single punctuation mark or stop word
            if (len(word) == 1 and word in string.punctuation) or word in STOP_WORDS_FR:
                continue
            
            #Todo : manage "y-a-t'il" case = double punctation mark in the same word
            for lettre in word:
                if lettre not in string.punctuation:
                    word_to_add = True
                    continue
                else:
                    # if there is punctation mark in the word, split the words
                    word_split = word.split(lettre)
                    # And add each of them into the new list
                    for elt in word_split:
                        if elt in STOP_WORDS_FR:
                            continue
                        else:
                            cleaned_sentence.append(elt)
                    # The word is already added to the list
                    word_to_add = False
                    # Stop to analyze the current word, and pass to the following word 
                    break       
            
            # If the word had not punctation mark, add the word into the new list
            if word_to_add:
                cleaned_sentence.append(word)

        if not cleaned_sentence:
            raise ValueError("Sentence doesn't contain words")

        # Get the last word of the list
        adress_word = cleaned_sentence[-1]

        return adress_word
