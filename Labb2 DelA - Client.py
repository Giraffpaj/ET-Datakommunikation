# UDP Client
# Anders Nelsson ET1530 BTH
# Exempel från kursbok
import time
from socket import *
#serverName = 'hostname'
reciever = '193.11.185.113'

def procedure():
    time.sleep(0.00)  ##skall vara 149 för perfekt överföreing


serverPort = 80

# create UDP socket
clientSocket = socket(AF_INET, SOCK_DGRAM)

# get input from keyboard
message = 'kaka'

count = 0
while (time.clock() <= 15.0 and count <=100000):
    message = str(count)
    clientSocket.sendto(message.encode(),(reciever, serverPort))
    count = count +1
    procedure()

# close UDP socket
message = 'Session ended'
clientSocket.sendto(message.encode(),(reciever, serverPort))
message = 'time in seconds:' + str(time.clock())
clientSocket.sendto(message.encode(),(reciever, serverPort))
clientSocket.close() 

print ('Session Ended')

