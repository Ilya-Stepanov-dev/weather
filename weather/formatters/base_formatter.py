from typing import override
from log import log_decorator

from models.weather import Weather

class WeatherFormatter:

    @override
    @log_decorator
    def format_weather(self) -> str:
        raise NotImplementedError

def format_weather(weather: Weather, formatter: WeatherFormatter) -> str:
    return formatter.format_weather(weather)