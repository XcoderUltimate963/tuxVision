#!/usr/bin/python3.8

import sys
import guiOfApp
import dataCommu

def main():
    guiObj = guiOfApp.guiForApp("Naruto Face Recognition", 800, 507)
    guiObj.load_window()

def setUpDataCommu(host=None, port=None, option=None):
    #some data commu work here
    dcObj = dataCommu.dataCommu(host, port)
    dcObj.connectToServer()
    return dcObj

if __name__ == "__main__":
	main()
