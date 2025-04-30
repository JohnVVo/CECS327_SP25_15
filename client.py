import socket as socket

maxBytesToReceive = 1024

if __name__ == "__main__":
    
    TCPSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Create the TCP Socket

    # Prompt and validate IP Address
    while True:
        serverIP = input("Enter Server IP Address: ") # Prompt user for IP Address
        try:
            socket.inet_aton(serverIP) # Validate IP Address
            break
        except socket.error:
            print("Invalid IP Address")

    # Prompt and Validate Server Port student ID, mac address, 
    while True:
        try:
            serverPort = int(input("Enter Server Port Number: ")) #Prompt user for Port Number of the server
            if 0 <= serverPort <= 65535:
                break
            else:
                print("Invalid Server Port (Not in Range, 0-65535)")
        except ValueError:
            print("Invalid Server Port (Not an Integer)")
    
    # Connect to Server
    TCPSocket.connect((serverIP, serverPort))
    
    # Sends message(s) to the server
    while True:
        message = input("""\n
        1. What is the average moisture inside my kitchen fridge in the past three hours?\n
        2. What is the average water consumption per cycle in my smart dishwasher?\n
        3. Which device consumed more electricity among my three IoT devices (two refrigerators and a dishwasher)?\n
        Please enter your query [1-3]: """)
        while message not in ["1", "2", "3", "quit"]:
            message = input("""Sorry, this query cannot be processed. Please try one of the following:\n
        1. What is the average moisture inside my kitchen fridge in the past three hours?\n
        2. What is the average water consumption per cycle in my smart dishwasher?\n
        3. Which device consumed more electricity among my three IoT devices (two refrigerators and a dishwasher)?\n
        Please enter your query [1-3]: """)

        TCPSocket.send(message.encode()) # Send message to the server
        if message.lower() == "quit":
            break
        serverResponse = TCPSocket.recv(maxBytesToReceive) # Receive response from server
        print("Server response: ", serverResponse.decode())
    
    # Close access to the server when finished
    TCPSocket.close()
