"""
M2M Lab Exercise 3
- Client that sends the TCP requests 
(Random Values of Temperature and Humidity) to the Server

Built by - Shubh Pathak (MSM19B018)
"""
import socket,time,random

HEADER = 64
PORT = 10001

SERVER = socket.gethostbyname(socket.gethostname()) # Automatically gets the Local IP Address
server_address = (SERVER,PORT)

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(server_address)

# Sends the request to Server
def send(message):
    print(f"Sending {message} (Temperature,Humidity) to Server")
    message =  message.encode('utf-8')
    client.send(message)


if __name__ == '__main__':
    try:
        while True:
            temperature = random.randint(1,50)
            humidity = random.randint(0,100)
            message = f"{temperature},{humidity}"
            send(message)
            time.sleep(1)
    except:
        print("\nStopped Sending requests to Server...")
    finally:
        client.close()


