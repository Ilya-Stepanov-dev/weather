from enum import Enum
from pydantic import BaseModel

class Role(Enum):
    user = 'user'
    assistant = 'assistant'


class ModelType(Enum):
    GPT4o = "gpt-4o-mini"
    Claude = "claude-3-haiku-20240307"
    Llama = "meta-llama/Meta-Llama-3.1-70B-Instruct-Turbo"
    Mixtral = "mistralai/Mixtral-8x7B-Instruct-v0.1"

class Message():
    role: Role
    content: str


class History(BaseModel):
    model: ModelType
    messages: list[Message]

    # def add_request(self, message: str):
    #     self.messages.append(Message(role=Role.user, content=message))
    
    # def add_response(self, message: str):
    #     self.messages.append(Message(role=Role.assistant, content=message))
    