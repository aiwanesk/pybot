""" BotAnswer class : give a pseudo life to the bot """

from random import choice

class BotAnswer():
    """
    Create a dictionnary of random answer by category
    Return a random answer choosen by category
    """

    def __init__(self):
        self.answer = {
            "address_answer": [
                "Salut mon bichon :) ",
                "Bonjour toi ! Comment ça va aujourd'hui ? ",
                "Hey, je suis ravie de te voir à nouveau ! Alors "
            ],
            "wiki_answer": [
                "Mais au fait, je ne t'ai pas dit : ",
                "Pour ta culture, tu sauras que ",
                "Le savais-tu ? "
            ],
            "error_answer": [
                "J'ai beau fouiller... ",
                "D'où sors-tu cela toi ? ",
                "Là tu me poses une colle ! "
            ]
        }

    def _random_answer(self, answer_type):
        """ Return a random answer by category (address, wiki, error) """

        if answer_type == "address":
            return choice(self.answer["address_answer"])
        elif answer_type == "wiki":
            return choice(self.answer["wiki_answer"])
        elif answer_type == "error":
            return choice(self.answer["error_answer"])

    @property
    def random_address_answer(self):
        """ Return a random address answer """
        return self._random_answer("address")

    @property
    def random_wiki_answer(self):
        """ Return a random wiki answer """
        return self._random_answer("wiki")

    @property
    def random_error_answer(self):
        """ Return a random error answer """
        return self._random_answer("error")
