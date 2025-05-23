from datetime import datetime
import requests
from countryinfo import CountryInfo
parameters = {
    'appid': 'your-api',
    'units': 'metric',
    'lang': 'ru'
}


def weather_info(city):
    parameters['q'] = city
    try:
        weather = requests.get('https://api.openweathermap.org/data/2.5/weather', params=parameters).json()
        name = weather['name']
        temp = weather['main']['temp']
        description = weather['weather'][0]['description']
        wind_speed = weather['wind']['speed']
        timezone = weather['timezone']
        sunrise = datetime.utcfromtimestamp(weather['sys']['sunrise'] + timezone).strftime('%H:%M:%S  %d.%m.%Y')
        sunset = datetime.utcfromtimestamp(weather['sys']['sunset'] + timezone).strftime('%H:%M:%S  %d.%m.%Y')

        return f'''🌤 Погода в городе {name}:
Описание: {description}
🌡 Температура: {temp}°C
💨 Скорость ветра: {wind_speed} м/с
🌅 Рассвет: {sunrise}
🌇 Закат: {sunset}'''

    except Exception as e:
        return 'Вы ввели некорректный город. Попробуйте снова.'


def country_info(item):
    country = CountryInfo(item)
    return f'''Название Страны: {country.name()}
Столица: {country.capital()}
Население: {country.population()}
Площадь: {country.area()}
Регион: {country.subregion()}'''

