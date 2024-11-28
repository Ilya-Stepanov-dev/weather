from typing import override

from log import log_decorator
from models.weather import Weather
from models.coordinates import Coordinates

class WeatherService:

    @override
    @log_decorator   
    def get_all_weather(self) -> Weather:
        raise NotImplementedError

@log_decorator
def get_all_weather(coordinates: Coordinates, service: WeatherService) -> Weather:
    service.lat = coordinates.lat
    service.lon = coordinates.lon
    return service.get_all_weather()