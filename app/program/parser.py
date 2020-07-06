"""This file contains the user input parser"""
import re
import unicodedata
from app.program.stop_words import STOP_WORDS


class Parser:
    """ User question parsing class """

    def __init__(self, question):
        self.question = question

    def parse(self):
        """ Parsing function """
        # Sets words in lowercase
        self.question = self.question.lower()
        # Removes accents
        self.question = ''.join((word for word in unicodedata.normalize('NFD', self.question)
                                 if unicodedata.category(word) != 'Mn'))
        # Removes punctuation and converts the question in a list of words
        self.question = re.sub(r'[^\w]', ' ', self.question).split()
        # Isolates keywords
        self.question = [word for word in self.question if word not in STOP_WORDS]
        # Converts the list into a string
        self.question = " ".join(self.question)
        return self.question
