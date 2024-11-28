from log import log_decorator
from .base_formatter import WeatherFormatter
from models.weather import Weather
from utils.datetime_formatter import format_datetime


class BaseFormatter(WeatherFormatter):
    
    @log_decorator
    def format_weather(self, data: dict | Weather) -> str:
        # if isinstance(data, Weather):
        data = data.model_dump()
        data['sys']['sunrise'] = format_datetime(data['sys']['sunrise'])
        data['sys']['sunset'] = format_datetime(data['sys']['sunset'])
        return data