import socket
import threading

clients = []

def handle_client(client):
    while True:
        try:
            msg = client.recv(1024)
            if not msg:
                break

            # send message to all other clients
            for c in clients:
                if c != client:
                    c.send(msg)
        except:
            break

    clients.remove(client)
    client.close()

# create server
server = socket.socket()
server.bind(('localhost', 55555))
server.listen()

print("Server running...")

while True:
    client, addr = server.accept()
    print("Connected:", addr)

    clients.append(client)

    thread = threading.Thread(target=handle_client, args=(client,))
    thread.start()