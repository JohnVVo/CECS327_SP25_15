import socket as socket
import psycopg2
import psycopg2.extras


maxBytesToReceive = 1024
neonDB_connection_string = f"postgresql://neondb_owner:npg_FqAQjlxe47SM@ep-withered-art-a52mqq69-pooler.us-east-2.aws.neon.tech/neondb?sslmode=require"

# Connect to NeonDB
try:
    db = psycopg2.connect(neonDB_connection_string)
    cursor = db.cursor(cursor_factory=psycopg2.extras.DictCursor)
except Exception as e:
    print(f"Error connecting to NeonDB: {e}")

def fetch_from_neonDB(query):
    try:
        # Execute the query
        cursor.execute(query)

        # Find matches to query
        results = cursor.fetchall()    

        return results
    except Exception as e:
        return f"Error executing query: {e}"

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
    print("Server listening on Port", Port)

    # Accept connection(s)
    incomingSocket, incomingAddress = ServerTCPSocket.accept() # Saves socket and address of incoming connection
    print(f"Accepted connection from {incomingAddress}")
    while True:
        query = incomingSocket.recv(maxBytesToReceive).decode() # Receive message from incoming connection (client)
        print(f"Received: {query.lower()}")
        if query.lower() == "1": #Query 1 triggered
            res = fetch_from_neonDB(
                '''
                SELECT (payload->>'Moisture Meter - MoistureMeter')::float
                FROM "IOT_virtual"
                WHERE payload->>'topic' = 'device/SmartFridge'
                AND to_timestamp((payload->>'timestamp')::bigint) >= NOW() - INTERVAL '3 hours'
                ''')
            sum = 0
            for moistureVal in res:
                sum += float(moistureVal[0])
            res = sum / len(res)
        elif query.lower() == "2": #Query 2 triggered
            res = "Calculate response for query 2"
        elif query.lower() == "3": #Query 3 triggered
            res = "Calculate response for query 3"
        elif query.lower() == "quit": #if the client terminates, then an empty message is sent, this is caught to end the connection
            break
        print(f"Returning: {res}")
        # res = fetch_from_neonDB(
        #     '''
        #     SELECT * FROM "IOT_virtual" 
        #     ORDER BY id DESC 
        #     LIMIT 5;
        #     ''')
        # for row in res:
        #     print(row['topic'], row['payload'])
        incomingSocket.send(str(res).encode()) # Sends reply to client
    # Close access to client socket when finished
    print("Connection Terminated")
    incomingSocket.close()
    # Close the connection to NeonDB
    cursor.close()
    db.close()
