"""
M2M Lab Exercise 3
- Server that accepts TCP requests from Single Client and
  logs them into datalog.csv file

Built by - Shubh Pathak (MSM19B018)
"""
import socket,csv

PORT = 10001
SERVER = socket.gethostbyname(socket.gethostname()) # Automatically gets the Local IP Address
server_address = (SERVER,PORT)

server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(server_address)


# Starts the Server
def run_server():
    server.listen()
    connection, address = server.accept()
    with open("datalog.csv","w") as f:
        writer = csv.writer(f)
        writer.writerow(['Temperature (in C)','Humidity (in %)'])
        while True:
            message = connection.recv(1024).decode('utf-8') # Receives Upto 1024 Bytes
            if not message:
                break
            data = message.split(',')
            
            print(f"Logging Temperature:{data[0]} C and Humidity:{data[1]} %")
            writer.writerow(data) # Logs the received data to datalog.csv file
    f.close()


if __name__ == '__main__':
    try:
        print("Started Accepting Requests...")
        run_server()
    except:
        print("\nStopping Server :(")
    finally:
        server.close()