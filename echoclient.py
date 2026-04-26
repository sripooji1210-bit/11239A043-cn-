import socket

def echo_client():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect to server
    s.connect(('127.0.0.1', 65432))

    while True:
        msg = input("Enter message (type 'exit' to quit): ")

        if msg == "exit":
            break

        s.sendall(msg.encode())

        data = s.recv(1024)
        print("Server replied:", data.decode())

    s.close()

if __name__ == "__main__":
    echo_client()