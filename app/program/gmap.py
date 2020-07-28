"""API google map file"""
import requests
from config import API_KEY


class Gmap:
    """Uses google's API to fetch coordinates and adress from a place"""
    def __init__(self, question):
        self.question = question
        self.url = 'https://maps.googleapis.com/maps/api/geocode/json?address='
        self.location = '&components=country:FR&key='
        self.key = API_KEY

    def search(self):
        """Search coordinates and adress"""
        try:
            req = requests.get(self.url + self.question +
                               self.location + self.key)

            result = req.json()
            short_adress = result['results'][0]['address_components'][1]['long_name']
            adress = result['results'][0]['formatted_address']
            lat = result['results'][0]['geometry']['location']['lat']
            lng = result['results'][0]['geometry']['location']['lng']
            return {'adress': adress, 'lat': lat, 'lng': lng, 'street': short_adress}

        except IndexError:
            return 'no result found'
