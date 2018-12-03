import json
import csv
import codecs
import urllib.request
from io import StringIO


csv_location = 'C:/Users/dell/Desktop/Python Leraning/Scraping/Forecast/cityidloc-20180625.csv'

token = 'TAkhjf8d1nlSlspN'
location = '119.141099,33.502869'  # Huai an

req = 'https://api.caiyunapp.com/v2/%s/%s/forecast.json' % (token, location)
json_response = urllib.request.urlopen(req).read()
json = json.loads(json_response)
if json.get('status') == 'ok':
    print(json.get('result').get('hourly').get('description'))
    value_now = json.get('result').get('hourly').get('skycon')[0].get('value')
    value_later = json.get('result').get('hourly').get('skycon')[7].get('value')
    if value_now == 'RAIN':
    	print('It is raining outside')
    elif value_later == 'RAIN':
    	print('It will rain in one hour')
else:
    print(json.get('error'))
