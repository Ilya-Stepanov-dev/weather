from dataclasses import dataclass
from pydantic import BaseModel

@dataclass(slots=True, frozen=True)
class Coordinates(BaseModel):
    lat: float
    lon: float
