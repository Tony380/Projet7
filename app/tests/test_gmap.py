"""This file contains the Google Maps api test"""
from app.program import gmap


question = "louvre"
test = gmap.Gmap()
response = {
    "results": [
        {
            'formatted_address': "Rue de Rivoli, 75001 Paris, France",
            'geometry': {
                'location': {
                    'lat': 48.8606111,
                    'lng': 2.337644
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
        test.search(question)
        assert test.location == {'adress': 'Rue de Rivoli, 75001 Paris, France', 'lat': 48.8606111, 'lng': 2.337644}
