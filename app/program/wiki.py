"""This file contains the wikipedia API"""
import wikipedia


class Wiki:
    """Wikipedia searching class"""

    def __init__(self, question):
        self.question = question
        """Set french language"""
        wikipedia.set_lang('fr')

    def search(self):
        """Return first 2 sentences of the wikipedia article and the page's url"""
        try:
            page = wikipedia.summary(self.question, sentences=2)
            url = wikipedia.page(self.question).url
            return {'page': page, 'url': url}

        except wikipedia.exceptions.PageError:
            return "no result found"

        except wikipedia.exceptions.DisambiguationError:
            return 'no result found'

        except IndexError:
            return "no result found"

        except KeyError:
            return 'no result found'
