"""This file contains the Google Maps api test"""
from app.program import wiki

question = "louvre"
content = 'Le musée du Louvre etc...'


class TestWiki:
    url = 'fake_url'


    def test_wiki(self, monkeypatch):

        def mock_summary(question, sentences):
            return content

        def mock_page(question):
            return TestWiki()


        monkeypatch.setattr(wiki.wikipedia, 'summary', mock_summary)
        monkeypatch.setattr(wiki.wikipedia, 'page', mock_page)
        test = wiki.Wiki(question)
        answer = test.search()
        assert answer == {'page': 'Le musée du Louvre etc...', 'url': 'fake_url'}

