# Server
import socket
import threading

my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
PORT = 8000
ADDRESS = "0.0.0.0"
broadcast_list = []

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
            args=(client,) #the list of argument for the function
        )
    client_thread.start()

def listen_thread(client):
    while True:
        message = client.recv(1024).decode()
        if message:
            print(f"Received message : {message}")
            broadcast(message)
        else:
            print(f"client has been disconnected : {client}")
            return

def broadcast(message):
    for client in broadcast_list:
        try:
            client.send(message.encode())
        except:
            broadcast_list.remove(client)
            print(f"Client removed : {client}")

# Function to send message from server
def send_message():
    while True:
        message = input("Server: ")
        broadcast(message)

# Start the server
accept_thread = threading.Thread(target=accept_loop)
accept_thread.start()

# Start thread to send message from server
send_message_thread = threading.Thread(target=send_message)
send_message_thread.start()
