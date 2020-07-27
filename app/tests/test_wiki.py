"""This file contains the Wikipedia api test"""
from app.program import wiki

question = "louvre"
result = {'query': {'pageids': ['fake_page_id'], 'pages': {'fake_page_id': {'pageid': 'fake_page_id',
                                                                            'extract': "fake_page"}}}}

link = 'http://fr.wikipedia.org/?curid=fake_page_id'


class TestWiki:


    def json(self):
        return result

    def test_search(self, monkeypatch):
        """Wikipedia api test with monkeypatch"""

        def mockreturn(url, params):
            return TestWiki()

        monkeypatch.setattr(wiki.requests, 'get', mockreturn)
        test = wiki.Wiki(question)
        answer = test.search()
        assert answer == {'page': 'fake_page', 'url': link}
