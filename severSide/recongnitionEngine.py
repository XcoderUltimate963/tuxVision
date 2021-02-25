import numpy as np
import cv2
from PIL import Image
import pickle

#will be keeping this here for future testing
#just testing now will implement classes and functions later

"""face_cascade = cv2.CascadeClassifier('cascade/data/haarcascade_frontalface_alt2.xml')
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("trainner.yml")

labels = {"person_name": 1}
with open("label.pickle", 'rb') as f:
	og_labels = pickle.load(f)
	labels = {v:k for k, v in og_labels.items()}

img = Image.open("DB/tempForRecog/index.jpeg")

img = np.array(img)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray, scaleFactor = 1.5, minNeighbors = 5)
for (x, y, w, h) in faces:
	#print(x, y, w, h)
	roi_gray = gray[y:y + h, x:x + w]
	roi_color = img[y:y + h, x:x + w]
	end_cord_x = x + w
	end_cord_y = y + h

	id, conf = recognizer.predict(roi_gray)
	if conf >= 0:
		print(id)
		print(labels[id])"""

class recognitionForFace:

	def __inti__(self):
		pass

	def recognizedData(self):
		returnValue = None
		self.face_cascade = cv2.CascadeClassifier('cascade/data/haarcascade_frontalface_alt2.xml')
		self.recognizer = cv2.face.LBPHFaceRecognizer_create()
		self.recognizer.read("trainner.yml")
		
		self.labels = {"person_name": 1}
		with open("label.pickle", 'rb') as f:
			og_labels = pickle.load(f)
			self.labels = {v:k for k, v in og_labels.items()}

		self.img = Image.open("DB/tempForRecog/index.jpeg")
		self.img = np.array(self.img)
		self.gray = cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)
		self.faces = self.face_cascade.detectMultiScale(self.gray, scaleFactor = 1.5,  minNeighbors = 1)	

		for (x, y, w, h) in self.faces:
			self.roi_gray = self.gray[y:y + h, x:x + w]
			self.roi_color = self.img[y:y + h, x:x + w]
			end_cord_x = x + w
			end_cord_y = y + h

			id, conf =  self.recognizer.predict(self.roi_gray)
			if conf >= 60:
				returnValue = str(self.labels[id])
			else:
				returnValue = "image is not recognized(reasons:- recognizer failed, image dosnt have associated data on the database)"

		return returnValue	 

def someRandomFunction():
	print("just typed cause i had to pretend to be typing and didnt kniw what to type")
