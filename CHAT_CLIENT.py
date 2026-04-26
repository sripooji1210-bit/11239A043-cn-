import socket
import threading

def receive(client):
    while True:
        try:
            msg = client.recv(1024).decode()
            print(msg)
        except:
            break

# create client
client = socket.socket()
client.connect(('localhost', 55555))

# receive thread
threading.Thread(target=receive, args=(client,), daemon=True).start()

while True:
    msg = input()
    client.send(msg.encode())