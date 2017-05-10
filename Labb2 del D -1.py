from socket import *
import time
serverPort = 80

serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('',serverPort))
count = 0


serverSocket.listen(1)

print ('The TCP server is ready to receive')
connectionSocket, addr = serverSocket.accept()
while count < 3000:
    sentence = connectionSocket.recv(1024).decode()
    print (sentence)
    count = count+1
    

connectionSocket.close()
