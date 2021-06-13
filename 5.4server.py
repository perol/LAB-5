import socket
import sys

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
PORT = 8888

serverSocket.bind(('', PORT))

serverSocket.listen(5)
print('Waiting for a connection...')


while True:
	connection, addr = serverSocket.accept()
	print("Connected to client")

	filename = connection.recv(1024)
	file = open(filename, "wb")

	msg = "Connected to: " + addr[0] + ", \n Thank You! \n"
	connection.send(msg.encode("utf-8"))

	rData = connection.recv(1024)
	while rData:
		file.write(rData)
		rData = connection.recv(1024)

	file.close()
	print("File has been copied and stored successfully")

	connection.close()
	print("Server close the connection \n")

	break
