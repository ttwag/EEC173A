# Import socket module
from socket import *    

# Use port 6789
serverPort = 6789

# Create a TCP server socket
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(("", serverPort))
serverSocket.listen(1)
print("The server is ready to receive...")

# Server should be up and running and listening to the incoming connections
while True:
    print('Ready to serve...')

    # Set up a new connection from the client
    connectionSocket, addr = serverSocket.accept()

    # If an exception occurs during the execution of try clause
    # the rest of the clause is skipped
    # If the exception type matches the word after except
    # the except clause is executed
    try:
        # Receives the request message from the client
        message =  connectionSocket.recv(1024).decode()

        # Extract the path of the requested object from the message
        # The path is the second part of HTTP header, identified by [1]
        filename = message.split()[1]

        # Because the extracted path of the HTTP request includes
        # a character '\', we read the path from the second character
        f = open(filename[1:], 'rb')

        # Store the entire content of the requested file in a temporary buffer
        outputdata = f.read()

        # Send the HTTP response header line to the connection socket
        response = "HTTP/1.1 200 SUCCESS\r\n\r\n"
        connectionSocket.send(response.encode())

        # Send the content of the requested file to the connection socket
        connectionSocket.sendall(outputdata)
        connectionSocket.close()

    except IOError:
        # Send HTTP response message for file not found
        # Fill in start
        response = "HTTP/1.1 404 ERROR\r\n\r\n"
        connectionSocket.send(response.encode())

        # Close the client connection socket
        connectionSocket.close()

serverSocket.close()  

