# UDP Client
# Anders Nelsson ET1530 BTH
# Exempel från kursbok
import time
from socket import *
#serverName = 'hostname'
reciever = '193.11.185.8'

import sys
message = 'tes100bytes100bytes100bytes100bytes100bytes100bytes100bytes100bytes100bytes'
number = sys.getsizeof(message)
print ('The Size of Message is: ' + str(number))
print ('Message will now be sent...')

#del 1
def procedure():
    time.sleep(0.09)


serverPort = 80

# create UDP socket
clientSocket = socket(AF_INET, SOCK_DGRAM)

count = 0
while (time.clock() <= 15.0 and count <= 100000):
    clientSocket.sendto(message.encode(),(reciever, serverPort))
    count = count +1
    procedure()



message = 'Session ended'
clientSocket.sendto(message.encode(),(reciever, serverPort))
message = 'time in seconds:' + str(time.clock())

print ('the number of messages was: ' + str(count))
clientSocket.sendto(message.encode(),(reciever, serverPort))
clientSocket.close() 

print ('Session Ended')

