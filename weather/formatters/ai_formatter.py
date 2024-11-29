from log import log_decorator
from .base_formatter import WeatherFormatter
from models.weather import Weather
from utils.datetime_formatter import format_datetime
from duck_ai_chat.api import AiChat
from duck_ai_chat.models import Message

class AIFormatter(WeatherFormatter):
    @log_decorator
    async def format_weather(self, data: dict | Weather) -> str:
        # if isinstance(data, Weather):
        data = data.model_dump()
        data['sys']['sunrise'] = format_datetime(data['sys']['sunrise'])
        data['sys']['sunset'] = format_datetime(data['sys']['sunset'])

        request = f"Я получил такие данные о погоде в формате JSON: \n{data}\nЧто можешь сказать о них? Дай совет как одеться. Ответь в формате дружеской беседы с братаном. И выведи все параметры в удобном виде."
        ai_chat = AiChat()
        await ai_chat.get_vqd()
        data = await ai_chat.send_request(message=Message(role="user", content=request))

        return data