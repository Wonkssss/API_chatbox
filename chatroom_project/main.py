from typing import Union, List
from fastapi import FastAPI, HTTPException
from datetime import datetime
import random
import json
from chatroom_project.models import Message, MessageOut, ChatroomIn, ChatroomOut
import atexit

app = FastAPI()

chatrooms = {}
chatroom_id = {}

def save_data():
    with open("chatrooms_data.json", "w") as json_file:
        json.dump(chatrooms, json_file)

# Function to load chatrooms data from a JSON file
def load_data():
    try:
        with open("chatrooms_data.json", "r") as json_file:
            return json.load(json_file)
    except FileNotFoundError:
        print("ERROR!!!!!!!!!!!!!")
        return {}
        

chatrooms = load_data()
atexit.register(save_data)


#create chatroom
@app.post("/chatrooms/{chatroom_name}")
def create_chatroom(chatroom_name: str):
    if chatroom_name in chatrooms:
        return {"chatroom_name": f"{chatroom_name} already exists"}
    chatrooms[chatroom_name] = []
    save_data()
    return {"chatroom_name": f"{chatroom_name} successfully created"}

#delete chatroom
@app.delete("/chatrooms")
def delete_chatroom(chatroom_name: str):
    if chatroom_name in chatrooms:
        del chatrooms[chatroom_name]
        return {"chatroom_name": f"{chatroom_name} successfully deleted"}
    save_data()
    return {"chatroom_name": f"{chatroom_name} does not exist"}

@app.get("/chatrooms/{chatroom_name}")
def get_chatrooms():
    return list(chatrooms.keys())


@app.get("/chatrooms/{chatroom_name}")
def get_chatroom(chatroom_name: str):
    if chatroom_name not in chatrooms:
        raise HTTPException(status_code=404, detail=f"Chatroom {chatroom_name} not found")
    return chatrooms[chatroom_name]


@app.get("/")
def read_root():
    return {"enter the chatroom": "http://localhost:5501/chatroom/{chatroom_name}"}


@app.post("/send_message")
def send_message(message: Message, chatroom_name: str) -> dict:
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    message_data = {
        "author": message.author,
        "message": message.message,
    }
    chatrooms[chatroom_name].append(message_data)
    save_data()
    return {"chatroom_name": chatroom_name, "message": "Message successfully sent", "data": message_data}



@app.get("/get_messages")
def get_messages():
    return chatrooms


#curl -X POST -H "Content-Type: application/json" -d '{"name": "Chatroom 1", "message": "Bonjour à tous", "body": "Un message", "author": "John"}' http://localhost:5501/send_message
#curl http://localhost:5501/chatrooms
#curl http://localhost:5501/get_messages


# detect process running on port and stop it
#lsof -i :5501
#kill -9 5501 #(<PID>)

#uvicorn chatroom_project.main:app --host 0.0.0.0 --port 5502 --reload
#uvicorn chatroom_project.main:app --host 127.0.0.1 --port 5502 --reload