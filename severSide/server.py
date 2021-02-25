import socket
import recongnitionEngine
import threading
import os
import json
import time

#FRFTU = File reading for temproray usage
#FRFPU = File reading for permanang usage

recogData = None
PROTOCOL = 4
PROTOFORMAT = 'utf-8'
PORT = 5050
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)

recogDataObj = recongnitionEngine.recognitionForFace()

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn, addr):
    print(f"[REQUEST FROM] {addr}.")
    
    connected = True
    while connected:
        protocol = conn.recv(PROTOCOL).decode(PROTOFORMAT)
        if (protocol):
            print(f"[NOTICE]: got a propoer proto from {protocol}")
            protocol = str(protocol)
        if protocol == "FRFT":
            print("image protocol is working")
            #returnmsg = "noice image boi!!!"
            with open('DB/tempForRecog/index.jpeg', 'wb') as f:
                while True:
                    data = conn.recv(512)
                    print("recieving")
                    if not data:
                        break
                    else:
                        f.write(data)
                f.close()
            print("breaking")
            #valObj = recogDataObj.recognitionForFace()
            valueTR = recogDataObj.recognizedData()
            data = {}
            data['ans'] = []
            data['ans'].append({
                'value': valueTR
            })
            with open("/home/xcoder963/Projects/perm/narutoFaceRecognition/file.json", "w") as file:
                json.dump(data, file)
            #data = valueTR.encode(PROTOFORMAT)
            
                file.close()
            #time.sleep(2)
            #conn.send(valueTR.encode(PROTOFORMAT))
        elif protocol == "FRFP":
            #will do this later
            dataToWrite = conn.recv(64).decode(PROTOFORMAT)
            index_IMG = None
            wasItemFound = False
            try:
                os.system(f"mkdir DB/stored/{dataToWrite}")
            except:
                print(f"[NOTICE]: Directory aready exist for {dataToWrite}")
            #will mayve right a json file to check if the category directory already exist
            #jsonFile = open("config.json", "r+")
            #json_data = json.load(jsonFile)
            """
            #will do this later
            for data in json_data["DB_ARR"]:
                if data == dataToWrite:
                    index_IMG = json_data[]
            """
            fileWhole = "DB/stored/%s/1.jpeg" % dataToWrite
            with open(fileWhole, 'wb') as f:
                while True:
                    data = conn.recv(512)
                    print("recieving")
                    if not data:
                        break
                    else:
                        f.write(data)
                f.close()
            print("breaking")
            os.system("python3 trainnerEngine.py")
            #recogData = "WRITTEN"
            #conn.send(f"{recogData}")
        elif protocol == 'TEST':
            print("protocol is working")
            returnmsg = "noice boi!!!"
            recieveMessage = conn.recv(256).decode(PROTOFORMAT)
            print(recieveMessage)
            conn.send(returnmsg.encode(PROTOFORMAT))
        elif protocol == 'TIMG':
            print("image protocol is working")
            returnmsg = "noice image boi!!!"
            with open('DB/tempForRecog/index.jpeg', 'wb') as f:
                while True:
                    data = conn.recv(512)
                    print("recieving")
                    if not data:
                        break
                    else:
                        f.write(data)
                f.close()
            #conn.send(returnmsg.encode(PROTOFORMAT))

def main():
    server.listen()
    print(f"[LISTENING]: Server is listening on {SERVER} at port {PORT}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target = handle_client, args = (conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTION]: {threading.activeCount() - 1}")

if __name__ == "__main__":
    print("[STARTING]: server is starting")
    main()
