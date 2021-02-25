import os
import cv2
import pickle
import numpy as np
from PIL import Image

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
image_dir = os.path.join(BASE_DIR, "DB/stored")

face_cascade = cv2.CascadeClassifier('cascade/data/haarcascade_frontalface_alt2.xml')
recognizer = cv2.face.LBPHFaceRecognizer_create()

current_id = 0
label_ids = {}
y_labels = []
x_train = []

for root, dir, files in os.walk(image_dir):
	for file in files:
		if file.endswith("jpeg") or file.endswith("png"):
			path = os.path.join(root, file)
			label = os.path.basename(os.path.dirname(path)).replace(" ", "_").lower()
			print(label, path)
			if not label in label_ids:
				label_ids[label] = current_id
				current_id += 1
			id = label_ids[label]
			print(label_ids)
			#y_labels.append(label)
			#x_train.append(path)
			pil_image = Image.open(path).convert("L")
			size = (400, 400)
			final_image = pil_image.resize(size, Image.ANTIALIAS)
			image_array = np.array(pil_image, "uint8")
			print(image_array)
			faces = face_cascade.detectMultiScale(image_array, scaleFactor = 1.5, minNeighbors = 1)
			for (x, y, w, h) in faces:
				roi = image_array[y:y + h, x:x + w]
				x_train.append(roi)
				y_labels.append(id)
print(y_labels)
print(x_train)

with open("label.pickle", "wb") as f:
	pickle.dump(label_ids, f)

recognizer.train(x_train, np.array(y_labels))
recognizer.save("trainner.yml")
