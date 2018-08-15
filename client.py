import socket
import time
import os


server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
server.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
# Set a timeout so the socket does not block
# indefinitely when trying to receive data.
server.settimeout(0.2)
server.bind(("", 44444))
message = b"test result 2"

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
client.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
client.bind(("", 37020))
while True:
 data, addr = client.recvfrom(1024)
 print("received message: %s"%data)
 #do something
 os.system("./test.sh")
 server.sendto(message, ('<broadcast>', 37021))
 print("result message sent!")
