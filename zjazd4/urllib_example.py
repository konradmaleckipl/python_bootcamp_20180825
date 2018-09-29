import urllib.request
import json
import datetime
import sys


def get_city_weather(woeid):
    f = urllib.request.urlopen(f'https://www.metaweather.com/api/location/{woeid}/')
    data = json.loads(f.read())
    for day in data['consolidated_weather']:
        if day['applicable_date'] == datetime.datetime.today().strftime('%Y-%m-%d'):
            return [day['the_temp'], day['air_pressure'], day['humidity']]


def get_woeid(city):
    f = urllib.request.urlopen(f'https://www.metaweather.com/api/location/search/?query={city}')
    data = json.loads(f.read())
    if len(data) < 1:
        return 0
    return data[0]['woeid']


if __name__ == "__main__":
    assert len(sys.argv) > 1, 'Prosze podac miasto jako argument!'
    city = sys.argv[1]
    woeid = get_woeid(sys.argv[1])
    if woeid == 0:
        print('Nie znaleziono takiego miasta!')
        sys.exit(1)
    day = get_city_weather(woeid)
    print(f"Pogoda w {city}:\n\t- temperatura: {day[0]} °C\n\t- ciśnienie: {day[1]} hPa\n\t- wilgotność: {day[2]}%")