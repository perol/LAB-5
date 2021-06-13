import socket
import os
import sys

host = "192.168.56.104"

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
port = 8888

serverSocket.connect((host, port))

sendFile = input("Enter filename send to server: ")
print("Filename: " + sendFile)

file = open(sendFile, "rb")
sendData = file.read(1024)

serverSocket.send(sendFile.encode("utf-8"))

while sendData:
	print("Received Message from server \n", serverSocket.recv(1024).decode("utf-8"))
	serverSocket.send(sendData)
	sendData = file.read(1024)

serverSocket.close()
