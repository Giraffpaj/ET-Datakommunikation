from socket import *
serverPort = 80
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))

print ("The UDP server is ready to recieve")

while True:
    message, clientAddress = serverSocket.recvfrom(2048)      
    print (message.decode())
    modifiedMessage = message.decode().upper()

