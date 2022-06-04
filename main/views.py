from django.shortcuts import render

import cv2

from PIL import Image

im = Image.open('a.jpg')
im.save('a.png')

# Create the haar cascade
faceCascade = cv2.CascadeClassifier('main/haarcascade_frontalface_default.xml')

# Read the image
image = cv2.imread('a.png')

# Detect faces in the image
# Detect faces
faces = faceCascade.detectMultiScale(image, 1.1, 4)


# Draw rectangle around the faces
for (x, y, w, h) in faces:
  cv2.rectangle(image, (x, y), (x+w, y+h), (255, 0, 0), 2)
  faces = image[y:y + h, x:x + w]
  cv2.imwrite('face.jpg', faces)
  pixel = cv2.resize(faces, (1,1))
  cv2.imwrite('pixel.jpg', pixel)
  print(pixel)

# Export the result
cv2.imwrite("face_detected.png", image)
print('Successfully saved')