"""This class uses google's API to fetch coordinates and adress from a place"""
import requests
from config import API_KEY


class Gmap:

    def __init__(self, question):
        self.question = question
        self.endpoint = 'https://maps.googleapis.com/maps/api/geocode/json?address='
        self.location = '&components=country:FR&key='
        self.key = API_KEY

    def search(self):
        """Search coordinates and adress"""
        try:
            r = requests.get(self.endpoint + self.question + self.location + self.key)
            result = r.json()
            adress = result['results'][0]['formatted_address']
            lat = result['results'][0]['geometry']['location']['lat']
            lng = result['results'][0]['geometry']['location']['lng']
            return {'adress': adress, 'lat': lat, 'lng': lng}

        except IndexError:
            return 'no result found'
