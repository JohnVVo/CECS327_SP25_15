import socket as socket

maxBytesToReceive = 1024

if __name__ == "__main__":
    
    # Create the TCP Socket
    ServerTCPSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Prompt and validate IP Address ()
    while True:
        IP = input("Enter Server IP Address: ") # Prompt user for IP Address
        try:
            socket.inet_aton(IP) # Validate IP Address
            break
        except socket.error:
            print("Invalid IP Address")

    # Prompt and Validate Server Port
    while True:
        try:
            Port = int(input("Enter Port Number: ")) #Prompt user for Port Number of the server
            if 0 <= Port <= 65535:
                break
            else:
                print("Invalid Server Port (Not in Range, 0-65535)")
        except ValueError:
            print("Invalid Server Port (Not an Integer)")

    # Bind the socket to an IP & Port
    ServerTCPSocket.bind((IP, Port))

    # Listen for connections
    ServerTCPSocket.listen(5) # 5 = number of clients allowed per queue

    # Accept connection(s)
    incomingSocket, incomingAddress = ServerTCPSocket.accept() # Saves socket and address of incoming connection
    print(f"Accepted connection from {incomingAddress}")
    while True:
        query = incomingSocket.recv(maxBytesToReceive).decode() # Receive message from incoming connection (client)
        print(f"Received: {query.lower()}")
        if query.lower() == "1": #Query 1 triggered
            response = "Calculate response for query 1"
        elif query.lower() == "2": #Query 2 triggered
            response = "Calculate response for query 2"
        elif query.lower() == "3": #Query 3 triggered
            response = "Calculate response for query 3"
        elif query.lower() == "quit": #if the client terminates, then an empty message is sent, this is caught to end the connection
            break
        print(f"Returning: {response}")
        incomingSocket.send(response.encode()) # Sends reply to client
    # Close access to client socket when finished
    print("Connection Terminated")
    incomingSocket.close()
