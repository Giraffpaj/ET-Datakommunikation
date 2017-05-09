from socket import *
serverPort = 80
sequenceNumber = 0
oldMessage = 0
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))

print ("The UDP server is ready to recieve")

while True:
    message, clientAddress = serverSocket.recvfrom(2048)      
    if oldMessage != int(message):
        print('wrong order')
        oldMessage = int(message)
        
    oldMessage = oldMessage+1

    print (message.decode()+ ';')

    modifiedMessage = message.decode().upper()

