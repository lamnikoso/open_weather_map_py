import requests
from datetime import datetime

API = '11c0d3dc6093f7442898ee49d2430d20'
URL = 'http://api.openweathermap.org/data/2.5/weather'
TEMPLATE = '''Current weather in {city} for {timedate}:
temperature is {temperature} Celsius
pressure is {pressure} hPa
humidity is {humidity} %
wind speed is {wind_speed} meter/sec
clouds is {clouds} %
id city is {id_city}'''

def main():
    city = ''
    while city != 'exit':
        city = input('Please, write your city: ').strip()

        if city == 'exit':
            break

        params = {
            'q': city,
            'appid': API,
            'units': 'metric',
            'lang': 'ru',
        }

        res = requests.get(URL, params=params)

        if res.status_code == 200:
            data = res.json()
            print(TEMPLATE.format(city=data["name"], id_city=data["id"], temperature=data["main"]["temp"], pressure=data["main"]["pressure"], humidity=data["main"]["humidity"], timedate=datetime.now().strftime('%H:%M:%S %d/%m/%Y'), wind_speed=data["wind"]["speed"], clouds=data["clouds"]["all"]))

if __name__ == '__main__':
    main()
