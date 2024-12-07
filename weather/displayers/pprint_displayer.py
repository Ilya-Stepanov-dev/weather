import pprint

from log import log_decorator
from .base_displayer import Displayer
from models.weather import Weather


class PprintDisplayer(Displayer):

    @log_decorator
    def display_weather(self, data) -> None:
        pprint.pprint(data)