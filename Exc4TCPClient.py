from socket import *

while True:
    # serverName = "10.200.130.62"
    serverName = "localhost"
    serverPort = 12000
    # serverName = input("Input server: ")
    # serverPort = input("Input port (recommended: 12000): ")
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((serverName, int(serverPort)))
    print("Working Commands: Random, Add, Subtract")
    sentence = input("Input command: ")
    clientSocket.send(sentence.encode())
    sentence = input("Input first number: ")
    clientSocket.send(sentence.encode())
    sentence = input("Input second number: ")
    clientSocket.send(sentence.encode())


    modifiedSentence = clientSocket.recv(1024)
    print("Server sends: ", modifiedSentence.decode())
    
