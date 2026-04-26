import socket

s = socket.socket()
s.connect(("example.com", 80))

request = "GET / HTTP/1.1\r\nHost: example.com\r\n\r\n"
s.send(request.encode())

while True:
    data = s.recv(4096)
    if not data:
        break
    print(data.decode(), end="")

s.close()