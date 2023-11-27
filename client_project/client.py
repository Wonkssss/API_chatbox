from datetime import datetime 
import requests
import json


chatrooms = {}
data = {}
current_chatroom = None


def choose_or_create_chatroom():
    global chatrooms, data
    chatroom_name = input("enter the name of an existing chatrooms or create one with c: ")
    if chatroom_name == "c":
        chatroom_name = input("enter the name of the new chatrooms : ")
        data = {"name": chatroom_name, "messages": []}
        url = f"http://localhost:5501/chatrooms/{chatroom_name}" 
        print(data)
        chatrooms[chatroom_name] = []
        print(chatrooms)
        response = requests.post(url, json=data)
        if response.status_code == 200:
            print(f"Chatroom successfully created! : {chatroom_name}")
            return chatroom_name
        else:
            print(f"Error when creating the chatrooms : {response.status_code} - {response.text}")
            return None
    else:
        url = f"http://localhost:5501/chatrooms/{chatroom_name}"
        response = requests.get(url, json=data)

        if response.status_code == 200:
            print(f"Chatroom successfully found! : {chatroom_name}")
            return chatroom_name
        else:
            print(f"Error when finding the chatrooms : {response.status_code} - {response.text}")
            print("try again")
            return None
        

chatroom_name = choose_or_create_chatroom()
user = input("Entrez le nom de l'auteur : ")
current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

while True:
    message = input("Entrez un message (ou quit pour quitter) : ")
    if message == "quit":
        print("chatrooms: ", chatrooms)
        break
        


    url = f"http://localhost:5501/send_message?chatroom_name={chatroom_name}" ###
    data = {
    "author": user,
    "message": message,
    "date": current_time,
    "chatroom_name": chatroom_name

    }
    (chatrooms[chatroom_name]).append(data)
    print("chatrooms update: ", chatrooms)

    response = requests.post(url, json=data)

    if response.status_code == 200:
        print(f"Message successfully sent! : {message}")
    else:
        print(f"Error when sending the message : {response.status_code} - {response.text}")


"""
200 OK : La requête a réussi, et la réponse contient les données demandées.
201 Created : La ressource a été créée avec succès sur le serveur.
400 Bad Request : La requête est mal formulée ou incorrecte.
401 Unauthorized : L'accès à la ressource est refusé en raison de l'absence d'authentification ou de droits d'accès insuffisants.
404 Not Found : La ressource demandée n'a pas été trouvée sur le serveur.
500 Internal Server Error : Une erreur interne du serveur s'est produite."""

