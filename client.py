import socket

PORT = 10000
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER = socket.gethostbyname(socket.gethostname())

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


def start():
    try:
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
        except (ConnectionResetError, OSError) as e:
            print(f"Erro {e}. Server might have shut down") 
        finally:
            client.close()
            print("Disconnected from server.")
    except Exception as e:
        print(f"Unexpected error {e}. Could not connect to server") 

start()