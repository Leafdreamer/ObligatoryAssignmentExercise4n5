from socket import *

while True:
    # serverName = "10.200.130.62"
    serverName = "localhost"
    serverPort = 12000
    # serverName = input("Input server: ")
    # serverPort = input("Input port (recommended: 12000): ")
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((serverName, int(serverPort)))
    print("Example JSON format: {\"method\": \"Random\", \"Tal1\": 10, \"Tal2\": 20}")
    print("Working Commands: Random, Add, Subtract")
    sentence = input("Input JSON: ")
    clientSocket.send(sentence.encode())


    modifiedSentence = clientSocket.recv(1024)
    print("Server sends: ", modifiedSentence.decode())
    
