from socket import *
import threading
import random
import json

def handleClient(connectionSocket, addr):
    result = ""
    print("Connection successful")
    input = connectionSocket.recv(1024).decode()
    print(input)
    try:
        jsonInput = json.loads(input)
    except ValueError:
        result = "Invalid formatting."
    
    if result != "Invalid formatting.":
        if str(jsonInput["Tal1"]).isdigit() == False:
            if str(jsonInput["Tal2"]).isdigit() == False:
                result = "Both numbers are invalid."
            result = "First number is invalid."
        elif str(jsonInput["Tal2"]).isdigit() == False:
            result = "Second number is invalid."
        elif jsonInput["method"].lower() == "random":
            result = str(random.randint(jsonInput["Tal1"],jsonInput["Tal2"]))
        elif jsonInput["method"].lower() == "add":
            result = str(int(jsonInput["Tal1"]) + int(jsonInput["Tal2"]))
        elif jsonInput["method"].lower() == "subtract":
            result = str(int(jsonInput["Tal1"]) - int(jsonInput["Tal2"]))
        else:
            result = "Method is invalid."
    
    
    connectionSocket.send(result.encode())


serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print('Server is ready to listen')

while True:
    connectionSocket, addr = serverSocket.accept()
    threading.Thread(target=handleClient, args=(connectionSocket, addr)).start()