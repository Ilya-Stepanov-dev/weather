
import aiohttp

from log import log_decorator
from models.weather import Weather
from weather_services.base_services import WeatherService
from config import API_KEY_OPEN_WEATHER as api_key
from exceptions import FailedGetWeather

class OpenWeatherWeather(WeatherService):

    def __init__(self,
                 api_key: str = api_key,
                 lat: str = '56.99',
                 lon: str = '40.97',
                 units: str = 'metric',
                 lang: str = 'ru'):
        super().__init__()
        self.api_key = api_key
        self.lat = lat
        self.lon = lon
        self.units = units
        self.lang = lang

    @log_decorator
    async def get_all_weather(self) -> Weather:

        async with aiohttp.ClientSession() as session:
            response = await session.get(
                url=f'https://api.openweathermap.org/data/2.5/weather',
                params={
                    "lat": self.lat,
                    "lon": self.lon,
                    "appid": self.api_key,
                    "units": self.units,
                    "lang": self.lang,
                }
            )
            print(response)
            if response.status != 200:
                raise FailedGetWeather

            weather_data = await response.json()
            weather_data["weather"] = weather_data["weather"][0]

            return Weather.model_validate(obj=weather_data, strict=False)
