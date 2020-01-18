import cv2
import numpy as np
import imutils
from PIL import Image, ImageEnhance
import matplotlib.pyplot as plt

def imageAlter(image):
   alteredImage = Image.open(image)
   color = ImageEnhance.Color(alteredImage)
   alteredImage = color.enhance(0.5)
   contrast = ImageEnhance.Contrast(alteredImage)
   alteredImage = contrast.enhance(1.1)

   alteredImage.save("altered.jpg", "JPEG")
   return

def imageAnalyze(image):
   img = cv2.imread(image)
   cv2.namedWindow("original", cv2.WINDOW_NORMAL)
   cv2.namedWindow("CV", cv2.WINDOW_NORMAL)
   cv2.namedWindow("masked", cv2.WINDOW_NORMAL)

   hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

   # Accepted Colors
   #-----------
   #defining the Range of ??? color
   lower_range = np.array([110,50,50])
   upper_range = np.array([130,255,255])

   #defining the Range of Yellow color
   yellow_lower = np.array([212,192,121])
   yellow_upper = np.array([130,102,28])

   #defining the Range of Purple color
   purple_lower = np.array([125,104,161])
   purple_upper = np.array([49,39,63])

   #defining the Range of Green color
   green_lower = np.array([49,96,62])
   green_upper = np.array([23,48,29])

   #defining the Range of Red color
   red_lower = np.array([200,94,96])
   red_upper = np.array([51,22,26])

   #defining the Range of Black color
   black_lower = np.array([97,102,121])
   black_upper = np.array([38,38,38])

   #defining the Range of Blue color
   blue_upper = np.array([115,161,221])
   blue_lower = np.array([36,52,77])
  
   upper = np.array([200,255,200])
   lower = np.array([0,0,0])
   #-----------

   mask = cv2.inRange(hsv, lower,upper)
   imS = cv2.resize(img, (960, 540))
   imM = cv2.resize(mask, (960, 540))

   # cv2.imshow('CV', mask)
   cv2.imshow('original', img)

   for i in range(0,10):
      for i in range(0,3):
         upper[i] -= 10
         lower[i] += 5
      new_image = cv2.copyTo(img, mask)
      mask = cv2.inRange(hsv, lower,upper)

   cv2.imshow('masked', new_image)

   while(True):
      k = cv2.waitKey(5) & 0xFF
      if k == 27:
         break

   cv2.destroyAllWindows()
   
   return

imageAlter('RockPictures\\20200116_144936_flip.jpg')
# imageAlter("RockPictures\\20200116_143410.jpg")
imageAnalyze("altered.jpg")

def test(pic):

   image = cv2.imread(pic)
   print("The type of this input is {}".format(type(image)))
   print("Shape: {}".format(image.shape))
   plt.imshow(image)
   return

test('RockPictures\\20200116_144936_flip.jpg')