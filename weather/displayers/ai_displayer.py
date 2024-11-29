from log import log_decorator
from .base_displayer import Displayer
from models.weather import Weather


class AIDisplayer(Displayer):
    @log_decorator
    def display_weather(self, data) -> None:
        print(f'\n\n\nВаш помощник по погоде: \n{data}')