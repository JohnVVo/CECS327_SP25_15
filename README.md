﻿# End-to-End IOT System // Group 15

This project simulates an end-to-end IOT system by using a TCP client/server, a database and IoT sensor data from Dataniz to process and analyze user queries.

## Dependencies:
psycopg2 - Package needed for PostgreSQL connectivity.
While socket is imported into the server, it is part of Python's standard library and does not need to be installed.

## Initial Setup:
1. Clone the Repository
2. Install the dependencies
  - pip install psycopg2

## Running the Server:
1. Start the server by running the python file named "server.py"
2. Enter the IP Address and Port Number that will be binded to the server.
3. The server will listen for incoming client connections.
4. Once connected, the server will wait for a 1, 2 or 3 from the client. These numbers correspond with three predefined queries, where:
  - 1. Calculates the average moisture reading from the Smart Fridge in the last 3 hours.
  - 2. Calculates the average water consumption per cycle from the Smart Dishwasher over the past 12 cycles (24 hours total).
  - 3. Calculates which device had the highest electricity consumptions (in kWh) in the last 2 hours.
5. When the server receives a valid number, a SQL query will be generated based on the selected option. The server will then execute the query on the PostgreSQL database (NeonDB, in our case) to retrieve the data needed to answer the query.
6. When the server receives the string "quit", the connection will break.

## Running the Client:
1. Start the client by running the python file named "client.py"
2. Enter the IP Address and Port Number of the server you wish to connect to. If it is valid, it will connect.
3. If it connects, three predefined queries will pop up. Send the number corresponding with your desired query; If valid, it will encode that number and send it to the server.
4. To terminate the connection, simply type "quit" to break the connection.

## Database Configuration:
- The database is automatically connected within the server using psycopg2, so there is no need to manually configure the database. In the event you need to change which database the code pulls from (assuming it's still NeonDB), simply:
1. Go to the Project Dashboard of the database you want to connect
2. Click "Connect" and copy the connection string snippet
3. Open the server.py file in an IDE and replace the link in neonDB_connection_string with your own link.
