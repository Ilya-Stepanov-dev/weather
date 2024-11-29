from typing import override
from log import log_decorator

from models.weather import Weather

class Displayer():
    @override
    @log_decorator
    def display_weather(self, data):
        raise NotImplementedError
    
def display_weather(data, displayer: Displayer) -> None:
    return displayer.display_weather(data)
