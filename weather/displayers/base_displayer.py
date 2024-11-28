from typing import override
from log import log_decorator

from models.weather import Weather

class Displayer():
    @override
    @log_decorator
    def display_weather(self, weather: dict | Weather):
        raise NotImplementedError
    
def display_weather(data: Weather, displayer: Displayer) -> None:
    return displayer.display_weather(data)
