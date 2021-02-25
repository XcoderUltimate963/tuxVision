import socket
import main
import guiOfApp
import time
import json

#host = None
#port = None

class dataCommu:
    #will load some funtion to do data interaction stuff here
    
    def __init__(self, host=None, port=None):
        self.host = host
        self.port = port
    
    def connectToServer(self):
        try:
            self.closeSoc()
        except:
            print("")
        self.clientSoc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.clientSoc.connect((self.host, self.port))

        #while True:
        #	recievedData = self.clientSoc.recv()
        #	returnData(recievedData)

    def feedDataToServer(self, file_name, overHeadProTo):
        FORMAT = 'utf-8'
        #print(folder_name)
        protocol = overHeadProTo.encode(FORMAT)

        dcObj = guiOfApp.arrayOfObjects[0]
        dcObj.clientSoc.send(protocol)
        f = open(file_name, 'rb')
        l = f.read(512)
    
        while (l):
            dcObj.clientSoc.send(l)
            print("Sending")
            l = f.read(512)

        strH = "DoneWithT"
        #time.sleep(2)
        #dcObj.clientSoc.send(strH.encode(FORMAT))

        time.sleep(1)

        dataJ = None
        with open("/home/xcoder963/Projects/perm/narutoFaceRecognition/file.json", "r") as json_read:
            dataJ = json.load(json_read)
        json_read.close()
        guiOfApp.popup(dataJ)

        #dataValue = dcObj.clientSoc.recv(512).decode(FORMAT)
        #print(dataValue)

        self.closeSoc(dcObj)
    
        print("done")
        f.close()
        print("FINISISHING")

    def feedDataToServerT(self, file_name, folder_name, overHeadProTo):
        FORMAT = 'utf-8'
        #print(folder_name)
        protocol = overHeadProTo.encode(FORMAT)

        dcObj = guiOfApp.arrayOfObjects[0]
        dcObj.clientSoc.send(protocol)
        dcObj.clientSoc.send(folder_name.encode(FORMAT))
        f = open(file_name, 'rb')
        l = f.read(512)
    
        while (l):
            dcObj.clientSoc.send(l)
            print("Sending")
            l = f.read(512)

        strH = "DoneWithT"
        #time.sleep(2)
        #dcObj.clientSoc.send(strH.encode(FORMAT))

        time.sleep(1)

        self.closeSoc(dcObj)
    
        print("done")
        f.close()
        print("FINISISHING")

    def closeSoc(self, obj):
        obj.clientSoc.close()

#will return data from here to GUI
def returnData(returningData):
    print(returningData)
