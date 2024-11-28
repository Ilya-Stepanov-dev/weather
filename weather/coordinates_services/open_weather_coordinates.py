# import requests
import aiohttp

from log import log_decorator
from models.coordinates import Coordinates
from coordinates_services.base_services import CoordinatesService
from exceptions import FailedGeCoordinates
from config import API_KEY_OPEN_WEATHER as api_key

def get_city_from_user():
    city = input("Введите название города: ")
    if not city:
        return 'Ivanovo'
    return city

class OpenWeatherCoordinates(CoordinatesService):

    def __init__(self, 
                 api_key: str = api_key, 
                 city : str = get_city_from_user(),
                 lang : str = 'ru',
                 units : str = 'metric') -> None:
        super().__init__()
        self.api_key = api_key
        self.city = city
        self.lang = lang
        self.units = units
    
    @log_decorator
    async def get_coordinates(self) -> Coordinates:

        async with aiohttp.ClientSession() as session:
            response = await session.get(
                url=f'http://api.openweathermap.org/geo/1.0/direct?',
                params={
                    "q": self.city,
                    "lang": self.lang,
                    "units": self.units,
                    "appid": self.api_key,
                }
            )
            if response.status != 200:
                raise FailedGeCoordinates
            
            data = await response.json()
            print(data)

            return Coordinates.model_validate(obj=data[0], strict=False)