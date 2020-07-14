import requests
from config import API_KEY


class Gmap:

    def __init__(self):
        self.key = '&key=' + API_KEY
        self.endpoint = 'https://maps.googleapis.com/maps/api/geocode/json?address='
        self.location = {}

    def search(self, question):
        r = requests.get(self.endpoint + question + self.key)
        result = r.json()
        adress = result['results'][0]['formatted_address']
        lat = result['results'][0]['geometry']['location']['lat']
        lng = result['results'][0]['geometry']['location']['lng']
        self.location = {'adress': adress, 'lat': lat, 'lng': lng}
