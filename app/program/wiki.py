"""This file contains the wikipedia API"""
import wikipedia


class Wiki:
    """Wikipedia searching class"""

    def __init__(self, question, lat, lng):
        self.question = question
        self.lat = lat
        self.lng = lng
        """Set french language"""
        wikipedia.set_lang('fr')

    def search(self):
        """Return first 2 sentences of the wikipedia article and page's url"""
        try:
            wiki = wikipedia.geosearch(self.lat, self.lng, self.question)
            if not wiki:
                page = wikipedia.summary(self.question, sentences=2)
                url = wikipedia.page(self.question).url
                return {'page': page, 'url': url}
            else:
                page = wikipedia.summary(wiki[0], sentences=2)
                url = wikipedia.page(wiki[0]).url
                return {'page': page, 'url': url}

        except wikipedia.exceptions.PageError:
            return "no result found"

        except wikipedia.exceptions.DisambiguationError:
            return "no result found"

        except wikipedia.exceptions.WikipediaException:
            return 'no result found'

        except IndexError:
            return "no result found"

        except KeyError:
            return 'no result found'
