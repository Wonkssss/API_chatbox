
from pydantic import BaseModel
from typing import List
from datetime import datetime

class Message(BaseModel): #MessageIn
    message: str
    author: str

class MessageOut(BaseModel):
    message: str
    author: str
    date: datetime

class ChatroomIn(BaseModel):
    name: str


class ChatroomOut(BaseModel):
    uid : int
    name: str
    messages: List[MessageOut]

