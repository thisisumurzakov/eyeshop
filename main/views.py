import numpy as np
from django.core.files.storage import default_storage
from django.shortcuts import render

import cv2

from PIL import Image

# im = Image.open('a.jpg')
# im.save('a.png')
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework.views import APIView

from shop.models import Product
from shop.serializers import ProductListSerializer


class Picture_Upload(APIView):
  parser_classes = (MultiPartParser, FormParser,)

  def post(self, request):
    print(request.FILES)
    print(request.data)
    print(request.headers)
    print('thisisfiles')
    file = request.FILES['image']
    file_name = default_storage.save(file.name, file)
    file_url = default_storage.url(file_name)
    faceCascade = cv2.CascadeClassifier('main/haarcascade_frontalface_default.xml')
    bodyCascade = cv2.CascadeClassifier('haarcascade_fullbody.xml')
    # Read the image
    print(file_url)
    print('bu url')
    image = cv2.imread('/home/akbarbek/PycharmProjects/sense'+file_url)

    # Detect faces in the image
    # Detect faces
    faces = faceCascade.detectMultiScale(image, scaleFactor=1.1, minSize=(30, 30))



    # Draw rectangle around the faces
    shade = ''
    pixel = ''
    #for (x,y,w,h)
    for (x, y, w, h) in faces:
      cv2.rectangle(image, (x, y), (x + faces, y + h), (255, 0, 0), 2)
      faces = image[y:y + h, x:x + w]
      cv2.imwrite('face.jpg', faces)
      pixel = cv2.resize(faces, (1, 1))
      pixel_for_front = cv2.resize(pixel, (100, 100))
      cv2.imwrite('media/pixel.jpg', pixel_for_front)
      pixel = cv2.cvtColor(pixel, cv2.COLOR_BGR2GRAY)
      print(pixel)
      print('bupixel')
      cv2.imwrite('gray.jpg', pixel)
      pixel = pixel[0][0]
      print(pixel)
      if pixel <= 100:
        shade = 'Winter'
      elif pixel <= 150:
        shade = 'Autumn'
      elif pixel <= 171:
        shade = 'Summer'
      else:
        shade = 'Spring'

    products = Product.objects.filter(shade=shade).order_by('?')

    # Export the result
    cv2.imwrite("face_detected.png", image)
    print('Successfully saved')
    default_storage.delete('/home/akbarbek/PycharmProjects/sense'+file_url)
    print(shade)
    print(pixel)
    print(products)
    data = ProductListSerializer(products, many=True).data
    return Response(status=200, data=data)