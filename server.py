"""
M2M Lab Exercise 3
- Server that accepts TCP requests from Single Client and
  logs them into datalog.csv file

Built by - Shubh Pathak (MSM19B018)
"""
import socket

HEADERS = 64
PORT = 10001
SERVER = socket.gethostbyname(socket.gethostname()) # Automatically gets the Local IP Address
server_address = (SERVER,PORT)

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(server_address)


# Starts the Server
def run_server():
    server.listen()
    connection, address = server.accept()
    while True:
        message_length = int(connection.recv(HEADERS).decode('utf-8'))
        message = connection.recv(message_length).decode('utf-8')

        #  Logs the received data to datalog.csv file
        print(message)


if __name__ == '__main__':
    try:
        print("Started Accepting Requests...")
        run_server()
    except:
        print("\nStopping Server :(")