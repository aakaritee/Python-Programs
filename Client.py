from socket import *
serverName = 'localhost'
serverPort = 1234
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))

while True:

    sentence = input('Input lowercase sentence:')
    print('Client sent: ',sentence)
    clientSocket.send(sentence.encode())
    modifiedSentence = clientSocket.recv(1024)
    print('From Server: ',modifiedSentence.decode())


ServerSocket.close()