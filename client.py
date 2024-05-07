
import socket
import threading

client_name = input("Client Name : ").strip()
while not client_name:
    client_name = input("Your Name should not be empty : ").strip()

my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "0.0.0.0" # Server IP
port = 8000
my_socket.connect((host, port))

def send_message():
    while True:
        message_to_send = input()
        if message_to_send:
            message_with_nickname = client_name + " : " + message_to_send
            my_socket.send(message_with_nickname.encode())

def receive_message():
    while True:
        message = my_socket.recv(1024).decode()
        print(message)


send_message_thread = threading.Thread(target=send_message)
send_message_thread.start()

receive_message_thread = threading.Thread(target=receive_message)
receive_message_thread.start()
