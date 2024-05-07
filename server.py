import socket
import threading

my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
PORT = 8000
ADDRESS = "0.0.0.0" # Enter Server IP
broadcast_list = o

my_socket.bind((ADDRESS, PORT))

def accept_loop():
    while True:
        my_socket.listen()
        client, client_address = my_socket.accept()
        broadcast_list.append(client)
        start_listenning_thread(client)

def start_listenning_thread(client):
    client_thread = threading.Thread(
            target=listen_thread,
            args=(client,)
        )
    client_thread.start()
    
# Recieve all clients messages
def listen_thread(client):
    while True:
        message = client.recv(1024).decode()
        if message:
            print(f"\n{message}")
            broadcast(message)
        else:
            print(f"client has been disconnected : {client}")
            return
# Send messagee to all clients
def broadcast(message):
    for client in broadcast_list:
        try:
            client.send(message.encode())
        except:
            broadcast_list.remove(client)
            print(f"Client removed : {client}")

# Function to send message from server
def send_message():
    name = input("Server Name: ")
    while True:
        message = input("Message: ")
        broadcast(name + ": "+ message)

accept_thread = threading.Thread(target=accept_loop)
accept_thread.start()

send_message_thread = threading.Thread(target=send_message)
send_message_thread.start()
