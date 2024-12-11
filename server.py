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
        if not msg:
            print(f"Client {addr} has disconnected.")
            break
        print(f"Received from client {addr}: {msg}")
        if msg == DISCONNECT_MESSAGE:
            print(f"Client {addr} has disconnected.")
            break
    conn.close()

def send_messages(conn, addr):
    try:
        while True:
            msg = input("Send: ")
            conn.send(msg.encode('utf-8'))
    except (BrokenPipeError, ConnectionResetError):
        print(f"Connection with {addr} has been lost. Unable to send messages.")
    except Exception as e:
        print(f"An unexpected error while sending messages to {addr}: {e}")



def start():
    server.listen()
    while True:
        conn, addr = server.accept()
        receive_thread = threading.Thread(target=handle_client, args=(conn, addr))
        receive_thread.start()
        send_thread = threading.Thread(target=send_messages, args=(conn,addr))
        send_thread.start()
        # handle_client(conn, addr)
        print(f"Active connections: {threading.active_count() - 1}")
        


start()