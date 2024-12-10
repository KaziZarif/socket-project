import socket

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client.sendto(b"Hello world!", ("172.26.91.229", 10000)) # port 10000
