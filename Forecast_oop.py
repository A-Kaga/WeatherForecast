import json
import csv
import codecs
from urllib.request import urlopen


csv_location = 'C:/Users/dell/Desktop/Python Leraning/Scraping/Forecast/cityidloc-20180625.csv'
token = 'TAkhjf8d1nlSlspN'  # Test token for developer
location = '119.141099,33.502869'  # Huai an


class ColourfulCloud(object):

    def __init__(self, location, token):
        self.location = location
        self.token = token
        self.get_json()
        self.get_value()

    def get_json(self):
        req = 'https://api.caiyunapp.com/v2/%s/%s/forecast.json' % (
               self.token, self.location)
        json_response = urlopen(req).read()
        self.json = json.loads(json_response)
        if self.json.get('status') != 'ok':
            print(self.json.get('error'))

    def get_value(self):
        self.hourly_value = self.json.get('result').get('hourly')

        self.description_value = self.hourly_value.get('description')
        self.skycon_value = self.hourly_value.get('skycon')
        self.alert_value = {}
        if 'alert' in self.json.get('result'):
            self.alert_value = self.json.get('result').get('alert')

    def rain_report(self):
        if self.skycon_value[0].get('value') == 'CLOUDY':
            print('It is raining outside')
        elif self.skycon_value[1].get('value') == 'RAIN':
            print('It will rain in one hour')

    def alert_report(self):
        if self.alert_value != None:
            print(self.alert_value.get('content').get('description'))

weather = ColourfulCloud(location, token)
weather.rain_report()
