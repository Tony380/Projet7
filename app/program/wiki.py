import requests


class Wiki:

    def __init__(self, question):
        self.question = question
        self.url = 'https://fr.wikipedia.org/w/api.php'
        self.params = {'action': 'query',
                       'generator': 'search',
                       'prop': 'extracts',
                       'explaintext': 1,
                       'indexpageids': 1,
                       'exsentences': 2,
                       'gsrlimit': 1,
                       'gsrsearch': self.question,
                       'format': 'json'
                       }

    def search(self):
        try:
            response = requests.get(self.url, self.params)
            result = response.json()
            page_id = result['query']['pageids'][0]
            page = result['query']['pages'][page_id]['extract']
            url = 'http://fr.wikipedia.org/?curid=' + page_id
            return {'page': page, 'url': url}

        except IndexError:
            return "no result found"

        except KeyError:
            return 'no result found'
