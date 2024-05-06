import socket
import threading

nickname = input("Choose your nickname : ").strip()
while not nickname:
    nickname = input("Your nickname should not be empty : ").strip()

my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "localhost" # "127.0.1.1"
port = 8000
my_socket.connect((host, port))

# Function to send messages from client to server
def send_message():
    while True:
        message_to_send = input()
        if message_to_send:
            message_with_nickname = nickname + " : " + message_to_send
            my_socket.send(message_with_nickname.encode())

# Function to receive messages from server
def receive_message():
    while True:
        message = my_socket.recv(1024).decode()
        print(message)

# Start thread to send messages from client to server
send_message_thread = threading.Thread(target=send_message)
send_message_thread.start()

# Start thread to receive messages from server
receive_message_thread = threading.Thread(target=receive_message)
receive_message_thread.start()
