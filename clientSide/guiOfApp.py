import tkinter
from tkinter import ttk
import cv2
from PIL import Image, ImageTk
import dataCommu
import main

class guiForApp:
	#will load the Gui here with the constructor
	#will just pass basic params now will increase later
	def __init__(self, window_name, window_width, window_height):
		self.main_window = tkinter.Tk()
		self.main_window.title(window_name)
		self.main_window.maxsize(window_width, window_height)
		self.main_window.minsize(window_width, window_height)
		
		tab_parent = ttk.Notebook(self.main_window)

		takeData_tab = ttk.Frame(tab_parent)
		upload_tab = ttk.Frame(tab_parent)
		server_tab = ttk.Frame(tab_parent)
		help_tab = ttk.Frame(tab_parent)
		aboutUs_tab = ttk.Frame(tab_parent)

		tab_parent.add(takeData_tab, text = "Take Data")
		tab_parent.add(upload_tab, text = "Upload Data")
		tab_parent.add(server_tab, text = "Server TD")
		tab_parent.add(help_tab, text = "Help")
		tab_parent.add(aboutUs_tab, text = "About Us")
		
		#GUI for takeData_tab
		url_name = tkinter.Label(upload_tab, text = "Enter Image URL:-")
		image_name = tkinter.Label(upload_tab, text = "Enter the image name:-")
		
		url_entry = tkinter.Entry(upload_tab)
		image_entry = tkinter.Entry(upload_tab)
				
		buttonSubmit = tkinter.Button(upload_tab, text = "Submit", command = lambda: self.sendServerData(url_entry.get(), image_entry.get(), "FRFP"))
		
		url_name.grid(row = 0, column = 0, padx = 25, pady = 15)
		image_name.grid(row = 1, column = 0, padx = 25, pady = 15)
		
		url_entry.grid(row = 0, column = 1, padx = 25, pady = 15)
		image_entry.grid(row = 1, column = 1, padx = 25, pady = 15)

		buttonSubmit.grid(row = 2, column = 1, padx = 25, pady = 15)
		
		#GUI for upload_tab
		self.cap = cv2.VideoCapture(0)
		self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, 800)
		self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 250)

		self.lmain = tkinter.Label(takeData_tab)
		self.lmain.place(x = 75, y = 0)

		submitImageData = tkinter.Button(takeData_tab, text = "Submit", command = lambda: self.saveImage())
		submitImageData.place(x = 350, y = 400)

		self.show_frame()
		
		#GUI for serverTD_tab
		host_ip = tkinter.Label(server_tab, text = "Enter host ip address:-")
		port_number = tkinter.Label(server_tab, text = "Enter the port number:-")

		hostIp_entry = tkinter.Entry(server_tab)
		portNumber_entry = tkinter.Entry(server_tab)

		#funny how the word came out
		submitSTD = tkinter.Button(server_tab, text = "Submit", command = lambda: self.setServer_data(hostIp_entry.get(), int(portNumber_entry.get())))

		host_ip.grid(row = 0, column = 0, padx = 25, pady = 15)
		port_number.grid(row = 1, column = 0, padx = 25, pady = 15)

		hostIp_entry.grid(row = 0, column = 1, padx = 25, pady = 15)
		portNumber_entry.grid(row = 1, column = 1, padx = 25, pady = 15)

		submitSTD.grid(row = 2, column = 1, padx = 25, pady = 15)
		
		#GUI for help_tab
		help_text = tkinter.Label(help_tab, text = "sometextsometextsometext")
		help_text.place(x = 315, y = 100)
		
		#GUI for aboutUs_tab
		aboutUs_text = tkinter.Label(aboutUs_tab, text = "tools:-python3/Tkinter Programmer:-Xcoder Ultimate")
		aboutUs_text.place(x = 245, y = 100)

		tab_parent.pack(expand = 1, fill = 'both')

	def load_window(self):
		self.main_window.mainloop()
	
	def show_frame(self):
		_, self.frame = self.cap.read()
		self.frame = cv2.flip(self.frame, 1)
		cv2image = cv2.cvtColor(self.frame, cv2.COLOR_BGR2RGBA)
		img = Image.fromarray(cv2image)
		imgtk = ImageTk.PhotoImage(image = img)
		self.lmain.imgtk = imgtk
		self.lmain.configure(image = imgtk)
		self.lmain.after(10, self.show_frame)

	def sendServerData(self, url, name, protocol):
		dataC = dataCommu.dataCommu()
		dataC.feedDataToServerT(url, name, protocol)

	def setServer_data(self, host, port):
		#dataCommu.host = host
		#dataCommu.port = port
		dcObj = main.setUpDataCommu(host, port)
		storeObjS(dcObj)
	
	def saveImage(self):
		#will take text data later required
		frameT = self.cap.read()
		image_name = "itbs.png"
		cv2.imwrite("itbs.png", self.frame)
		getImageDataForRecog()
		print("someText")

def popup(msg=None):
	popup = tkinter.Tk()
	popup.wm_title("NAME")
	labelName = tkinter.Label(popup, text = msg)
	labelName.pack(side = "top", fill = "x", pady = 10)
	cBtn = tkinter.Button(popup, text = "close", command = popup.destroy)
	cBtn.pack()
	popup.mainloop()


arrayOfObjects = []

def storeObjS(objectH):
	arrayOfObjects.append(objectH)

def getImageDataForRecog():
	#will take image data from here for scanning on the server
	dataT = dataCommu.dataCommu()
	dataT.feedDataToServer("itbs.png", "FRFT")
	print("someText")
