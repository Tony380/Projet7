"""This file contains the Google Maps api test"""
from app.program import gmap

question = "louvre"
test = gmap.Gmap(question)
response = {
    "results": [
        {
            'formatted_address': "fake_adress",
            'geometry': {
                'location': {
                    'lat': 5000,
                    'lng': 5000
                }
            }
        }
    ]
}


class TestApi:

    def json(self):
        return response

    def test_search(self, monkeypatch):
        """Gmap api test with monkeypatch"""

        def mockreturn(url):
            return TestApi()

        monkeypatch.setattr(gmap.requests, 'get', mockreturn)
        answer = test.search()
        assert answer == {'adress': 'fake_adress', 'lat': 5000, 'lng': 5000}
