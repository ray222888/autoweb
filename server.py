import socket
import time
import ReadExcel
from time import sleep

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
server.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
# Set a timeout so the socket does not block
# indefinitely when trying to receive data.
server.settimeout(0.2)
server.bind(("", 44445))
message = b"test start"
server.sendto(message, ('<broadcast>', 37020))
print("message sent!")
#receive test result
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP
client.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
client.bind(("", 37021))
while True:
    data, addr = client.recvfrom(1024)
    print("received message: %s"%data)
    try:
     ReadExcel.excelUpdate(data)
    except Exception as ex: print (ex)
    sleep(2)