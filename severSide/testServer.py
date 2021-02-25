import socket
import time

PROTOCOL = 5
PORT = 5050
FORMAT = 'utf-8'
SERVER = "192.168.43.171"
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg, proto):
    message = msg.encode(FORMAT)
    protocol = proto.encode(FORMAT)
    finalProtocol = b' ' + protocol
    client.send(protocol)
    client.send(message)
    print(client.recv(1024).decode(FORMAT))
    
def sendImage(finalName, proto):
    protocol = proto.encode(FORMAT)
    client.send(protocol)
    f = open(finalName, 'rb')
    l = f.read(512)
    
    while (l):
        client.send(l)
        print("1")
        l = f.read(512)
    
    print("done")
    f.close()
    print("abc")
    #print(client.recv(1024).decode(FORMAT))

send("this should work", "TEST")
time.sleep(3)
sendImage("1.jpeg", "TIMG")

client.close()
