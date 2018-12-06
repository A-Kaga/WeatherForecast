import json
import csv
import codecs
import datetime
from urllib.request import urlopen
import requests


#csv_location = 'C:/Users/dell/Desktop/Python Leraning/Scraping/Forecast/cityidloc-20180625.csv'
token = 'your token'
location = 'your location'


class ColourfulCloud(object):

    def __init__(self, location, token):
        print('Init Starts')
        self.location = location
        self.token = token
        self.update()
        print('Init Get Ready')

    def update(self):
        self.get_json()
        self.get_value()


    def get_json(self):
        req = 'https://api.caiyunapp.com/v2/%s/%s/forecast.json' % (
            self.token, self.location)
        json_response = urlopen(req).read()
        print('Link Starts')
        self.json = json.loads(json_response)
        if self.json.get('status') != 'ok':
            print(self.json.get('error'))
        print('Json Get Ready')

    def get_value(self):
        self.hourly_value = self.json.get('result').get('hourly')

        self.description_value = self.hourly_value.get('description')
        self.pm25_value = self.hourly_value.get('pm25')
        self.skycon_value = self.hourly_value.get('skycon')
        self.temperature_value = self.hourly_value.get('temperature')
        self.alert_value = {}
        if 'alert' in self.json.get('result'):
            self.alert_value = self.json.get('result').get('alert')
        print('Value Get Ready')

    def rain_warning(self):
        url = 'https://maker.ifttt.com/trigger/rain_warning/with/key/b1-1FsKc9XxI48veEVHCoQ'
        value_dict = {}
        value_dict['value1'] = 'Just for test'
        if self.skycon_value[0].get('value') == 'RAIN':
            requests.post(url, json={'value1': 'It is raining outside'})
        elif self.skycon_value[1].get('value') == 'RAIN':
            requests.post(url, json={'value1': 'It will rain in one hour'})
        requests.post(url, json={'value1': 'It is raining outside'})
        print('rain_warning succeed!')

    def alert_report(self):
        if self.alert_value != None:
            print(self.alert_value.get('content').get('description'))

    def get_range(self):
        temperature_range = []
        pm25_range = []
        temp_list1 = []
        temp_list2 = []
        for rows in range(0, 15):
            temp_list1.append(self.temperature_value[rows].get('value'))
            temp_list2.append(self.pm25_value[rows].get('value'))

        temperature_range.append(min(temp_list1))
        temperature_range.append(max(temp_list1))
        pm25_range.append(min(temp_list2))
        pm25_range.append(max(temp_list2))

        print('Range Get Ready')
        return temperature_range, pm25_range


    def if_rain(self):
        for rows in range(0, 14):
            if self.skycon_value[rows].get('value') == 'RAIN':
                return 1
        return 0


    def daily_weather_report(self):
        range1, range2 = self.get_range()
        rain_range = ['No', 'Yes']
        value_dict = {}

        temperature_string = '%s℃ -- %s℃' %(range1[0], range1[1])
        pm25_string = 'Min:%s, Max:%s' %(range2[0], range2[1])
        rain_string = rain_range[self.if_rain()]

        value_dict['value1'] = temperature_string
        value_dict['value2'] = pm25_string
        value_dict['value3'] = rain_string

        print('Launch Get Ready')
        #url = 'https://maker.ifttt.com/trigger/daily_weather_report/with/key/b1-1FsKc9XxI48veEVHCoQ'
        url1 = 'https://maker.ifttt.com/trigger/daily_temperature_report/with/key/b1-1FsKc9XxI48veEVHCoQ'
        url2 = 'https://maker.ifttt.com/trigger/daily_pm25_report/with/key/b1-1FsKc9XxI48veEVHCoQ'
        url3 = 'https://maker.ifttt.com/trigger/daily_rain_report/with/key/b1-1FsKc9XxI48veEVHCoQ'

        requests.post(url1, json=value_dict)
        requests.post(url2, json=value_dict)
        requests.post(url3, json=value_dict)
        print('dailiy_report succeed!')


    def test(self):
        print(self.temperature_value)



weather = ColourfulCloud(location, token)
weather.daily_weather_report()
weather.rain_warning()
print('-------------------------------')
print('Congratulations! ALL SUCCEED!!!')

# old_time = datetime.datetime.now().hour
# while True:
#     current_time = datetime.datetime.now().hour
#     if old_time == current_time:
#         continue
#     elif current_time == 7:
#         weather.daily_weather_report()
#     else:
#         rain_warning()

#     old_time = current_time
