import json
import re
import aiohttp
# import asyncio
from models import ModelType, Message, History

class AiChat:
    def __init__(self,
        model: ModelType = ModelType.GPT4o,
        session: aiohttp.ClientSession | None = None,
        ) -> None:
        self.model = model
        self.session = session or aiohttp.ClientSession()
        self.vqd: str = ''
        self.history = History(model=model, messages=[])

    async def get_vqd(self) -> None:
        async with self.session.get(
                url="https://duckduckgo.com/duckchat/v1/status",
                headers={"x-vqd-accept": "1"},
            ) as response:
                if response.status != 200:
                    raise Exception(f"Failed to initialize chat: {response.status} {await response.text()}")
                if "x-vqd-4" in response.headers:
                    self.vqd = response.headers["x-vqd-4"]

    def _glue_response(self, response: str):
        pattern = r'data: ({.*?})'
        matches = re.findall(pattern, response)
        messages = []

        for match in matches:
            try:
                data = json.loads(match)
                if 'message' in data:
                    messages.append(data['message'])
            except json.JSONDecodeError:
                continue

        messages = ''.join(messages)
        return messages

    async def send_request(self, message: Message) ->str :
        self.history.messages.append(message)
        chat_url = "https://duckduckgo.com/duckchat/v1/chat"
        data = self.history.model_dump_json()
        headers = {
            "x-vqd-4": self.vqd,
            "Content-Type": "application/json",
            "Accept": "text/event-stream"
        }

        async with self.session.post(chat_url, headers=headers, data=data) as response:
            if response.status != 200:
                raise Exception(f"Failed to send message: {response.status} {await response.text()}")
            response = await response.text()
            response = self._glue_response(response)
            return response

# async def main():

#     chat = AiChat()
#     await chat.get_vqd()

#     while True:
#         user_input = input("You: ")
#         response = await chat.send_request(Message(role="user", content=user_input))
#         print(f"Assistant: {response}")

# if __name__ == "__main__":
#     import asyncio
#     asyncio.run(main())