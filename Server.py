from socket import *
import datetime
serverPort = 12000
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('',serverPort))
serverSocket.listen(5)
print('The W0695763 server is ready to receive')

currentDateTime = datetime.datetime.now()
currentTime = currentDateTime.strftime("%H:%M:%S")
CurrentDate = currentDateTime.strfTime("%Y:%M:%D")
IPHOSTNAME = socket.gethostname()
IP = socket.gethostbyname(IPHOSTNAME)

import socket
import re

while True:
    connectionSocket, addr = serverSocket.accept()
    sentence = connectionSocket.recv(1024).decode()

    capitalizedSentence = sentence.upper()

    print('W0695763 Server: Got' + sentence)

    if capitalizedSentence == 'HELO':
        connectionSocket.send('Hi, pleased to meet you.'.encode())
        print ( 'got ', capitalizedSentence )

    if capitalizedSentence == 'REQTIME':
        connectionSocket.send(CurrentTime.encode())
        print ('got ', capitalizedSentence)

    if capitalizedSentence == 'REQDATE':
        connectionSocket.send(Currentdate.encode())
        print ('got ', capitalizedSentence)

    if capitalizedSentence == 'ECHO blah':
        connectionSocket.send((re.sub('ECHO', sentence)).encode())
        print ('got ', capitalizedSentence)

    if capitalizedSentence == 'REQIP':
        connectionSocket.send(IP.encode())
        print ('got ', capitalizedSentence)

    if capitalizedSentence == 'BYE':
        connectionSocket.send('See you later!'.encode())
        print ('got ', capitalizedSentence)
        break;

#connectionSocket.send(capitalizedSentence.encode())

serverSocket.close()