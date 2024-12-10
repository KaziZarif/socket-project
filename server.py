import socket

sserver = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sserver.bind(("172.26.91.229", 10000)) # uses port 10000

while True:
    data, address = server.recvfrom(256)
    print ("Message from %s: %s" % (str(address), data))