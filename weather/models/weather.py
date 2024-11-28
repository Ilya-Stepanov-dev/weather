from dataclasses import dataclass
from enum import Enum
from typing import Optional
from pydantic import BaseModel, Field


type Celsius = float
type hPa = float
type Percent = float
type Meter = int
type Mm_h = float
type M_sec = float
type Deg = float
type Utc = int

class WeatherType(str, Enum):
    THUNDERSTORM = "Thunderstorm"
    DRIZZLE = "Drizzle"
    RAIN = "Rain"
    SNOW = "Snow"
    CLEAR = "Clear"
    FOG = "Fog"
    CLOUDS = "Clouds"

@dataclass(slots=True,frozen=True)
class Main(BaseModel):
    temp: Celsius
    feels_like: Celsius
    pressure: hPa
    humidity: Percent
    temp_min: Celsius
    temp_max: Celsius
    sea_level: hPa
    grnd_level: hPa

@dataclass(slots=True,frozen=True)
class DescriptionWeather(BaseModel):
    id: int
    main: WeatherType
    description: str
    icon: str

@dataclass(slots=True,frozen=True)
class Wind(BaseModel):
    speed: M_sec
    deg: Deg
    gust: M_sec

@dataclass(slots=True,frozen=True)
class Clouds(BaseModel):
    all: Percent

@dataclass(slots=True,frozen=True)
class Rain(BaseModel):
    h: Mm_h = Field(alias='1h')

@dataclass(slots=True,frozen=True)
class Show(BaseModel):
    h: Mm_h = Field(alias='1h')

@dataclass(slots=True,frozen=True)
class Sys(BaseModel):
    type: Optional[int] = None
    id: Optional[int] = None
    message: Optional[float] = None
    country: Optional[str] = None
    sunrise: Utc
    sunset: Utc

@dataclass(slots=True,frozen=True)
class Weather(BaseModel):
    main: Main
    weather: DescriptionWeather
    visibility: Meter
    clouds: Clouds
    sys: Sys
    rain: Optional[Rain] = None
    show: Optional[Show] = None
