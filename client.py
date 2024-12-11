import socket

PORT = 10000
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER = socket.gethostbyname(socket.gethostname())

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


def start():
    client.connect((SERVER, PORT))
    print(f"Connect to server at {SERVER}:{PORT}")
    try:
        while True:
            try:
                msg = input("Send: ")
            except EOFError:
                print("Diconnecting....")
                break

            client.send(msg.encode('utf-8'))
            
            if msg.upper() == DISCONNECT_MESSAGE:
                print("Disconnect message sent. Closing connection....")
                break 
    finally:
        client.close()
        print("Disconnected from server.")

start()