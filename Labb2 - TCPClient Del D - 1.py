# TCP Client
# Anders Nelsson ET1530 BTH
# Exempel från kursbok
import sys
import time
from socket import *
# serverName = 'hostname'
serverName = '193.11.185.8'
serverPort = 80
count = 0
message = '0;'

#sleepFunktion
def procedure():
    time.sleep(0.008)

# create TCP socket on client to use for connecting to remote server
clientSocket = socket(AF_INET, SOCK_STREAM)

# open the TCP connection
clientSocket.connect((serverName, serverPort))
sentence = 'Established Connection'
clientSocket.send(sentence.encode())

while (time.clock() <= 15.0 and count <= 3000):
    clientSocket.send(message.encode())
    count = count +1
    message = str(count) + ';'
    procedure()
    print ('message sent')

message = 'Session ended'
clientSocket.send(message.encode())
message = 'time in seconds:' + str(time.clock())

print ('the number of messages was: ' + str(count))
clientSocket.send(message.encode())

clientSocket.close()
