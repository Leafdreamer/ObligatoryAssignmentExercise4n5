from socket import *
import threading
import random

def handleClient(connectionSocket, addr):
    print("Connection successful")
    clientWants = connectionSocket.recv(1024).decode()
    print("Client sent command: " + clientWants)
    x = connectionSocket.recv(1024).decode()
    print("Client sent first number: " + x)
    y = connectionSocket.recv(1024).decode()
    print("Client sent second number: " + y)


    if clientWants.lower() == "random":
        result = str(random.randint(int(x),int(y)))
    elif clientWants.lower() == "add":
        result = str(int(x) + int(y))
    elif clientWants.lower() == "subtract":
        result = str(int(x) - int(y))
    else:
        result = "weh"
    
    connectionSocket.send(result.encode())


serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print('Server is ready to listen')

while True:
    connectionSocket, addr = serverSocket.accept()
    threading.Thread(target=handleClient, args=(connectionSocket, addr)).start()