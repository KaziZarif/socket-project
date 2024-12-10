import socket
import threading

PORT = 10000
SERVER = socket.gethostbyname(socket.gethostname())
DISCONNECT_MESSAGE = "!DISCONNECT"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("0.0.0.0", PORT)) # Listen on all available network interfaces

def handle_client(conn, addr):
    print(f"Connected to {addr}.")
    connected = True;
    while connected:
        msg = conn.recv(64).decode('utf-8')     # Receive 64 bytes of data from the client
        print(f"Received from client {addr}: {msg}")
        if msg == DISCONNECT_MESSAGE:
            print(f"Client {addr} has disconnected.")
            break
    conn.close()


def start():
    server.listen()
    while True:
        conn, addr = server.accept()
        # thread = threading.Thread(target=handle_client, args(conn, addr))
        # thread.start()
        handle_client(conn, addr)
        


start()