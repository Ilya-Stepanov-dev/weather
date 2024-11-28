from typing import override

from log import log_decorator
from models.coordinates import Coordinates

class CoordinatesService:
    @override
    @log_decorator
    def get_coordinates(self)-> Coordinates:
        raise NotImplementedError

@log_decorator
def get_coordinates(service: CoordinatesService):
    return service.get_coordinates()