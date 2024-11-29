import asyncio

from log import log_decorator

from models.weather import Weather
from models.coordinates import Coordinates
from weather_services.base_services import get_all_weather
from weather_services.open_weather import OpenWeatherWeather
from coordinates_services.base_services import get_coordinates
from coordinates_services.open_weather_coordinates import OpenWeatherCoordinates
from formatters.base_formatter import format_weather
from formatters.json_formatter import BaseFormatter
from formatters.ai_formatter import AIFormatter
from displayers.pprint_displayer import PprintDisplayer
from displayers.base_displayer import display_weather
from displayers.ai_displayer import AIDisplayer

@log_decorator
async def main():
    coordinates: Coordinates = await get_coordinates(OpenWeatherCoordinates())
    weather: Weather = await get_all_weather(coordinates=coordinates, service=OpenWeatherWeather())
    # formated_weather = format_weather(weather=weather, formatter=BaseFormatter())
    formated_weather = await format_weather(weather=weather, formatter=AIFormatter())
    # display_weather(data=formated_weather, displayer=PprintDisplayer())
    display_weather(data=formated_weather, displayer=AIDisplayer())
    
if __name__ == "__main__":
    asyncio.run(main())