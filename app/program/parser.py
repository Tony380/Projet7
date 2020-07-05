from app.program.config import STOP_WORDS
import re
import unicodedata


class Parser:
    """ User question parsing class """

    def __init__(self, question):
        self.question = question

    def parse(self):
        """ Parsing function """
        # Set words in lowercase
        self.question = self.question.lower()
        # Remove every accents
        self.question = ''.join((word for word in unicodedata.normalize('NFD', self.question)
                                 if unicodedata.category(word) != 'Mn'))
        # Remove punctuation and transform the question in a list of words
        self.question = re.sub(r'[^\w\s]', ' ', self.question).split()
        # Isolate keywords with list comprehension
        self.question = [word for word in self.question if word not in STOP_WORDS]
        # Transform the list into a string
        self.question = " ".join(self.question)
        return self.question
