"""This file contains the wikipedia API"""
import wikipedia


class Wiki:
    """Wikipedia searching class"""

    def __init__(self):
        """Set french language"""
        wikipedia.set_lang('fr')
        self.page = ''
        self.url = ''

    def search(self, question):
        """Return first 2 sentences of the wikipedia article and the page's url"""
        self.page = wikipedia.summary(question, sentences=2)
        self.url = wikipedia.page(question).url
