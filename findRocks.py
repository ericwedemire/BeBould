import cv2
import numpy as np
import imutils
from PIL import Image, ImageEnhance
import matplotlib.pyplot as plt
import random as rng
import math

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
   yellow_upper = np.array([30, 255, 255])
   yellow_lower = np.array([6,38,61])
   # yellow_upper = np.array([212,192,121])
   # yellow_lower = np.array([130,102,28])

   #defining the Range of Purple color
   purple_upper = np.array([125,104,161])
   purple_lower = np.array([49,39,63])

   #defining the Range of Green color
   green_upper = np.array([49,96,62])
   green_lower = np.array([23,48,29])

   #defining the Range of Red color
   red_upper = np.array([200,94,96])
   red_lower = np.array([51,22,26])

   #defining the Range of Black color
   black_lower = np.array([97,102,121])
   black_upper = np.array([38,38,38])

   #defining the Range of Blue color
   blue_upper = np.array([115,161,221])
   blue_lower = np.array([36,52,77])
  
   #-----------

   mask_blue = cv2.inRange(hsv,blue_lower,blue_upper)
   mask_green = cv2.inRange(hsv,green_lower,green_upper)
   mask_red = cv2.inRange(hsv,red_lower,red_upper)
   mask_yellow = cv2.inRange(hsv,yellow_lower,yellow_upper)
   mask_purple = cv2.inRange(hsv,purple_lower,purple_upper)
   temp1 = cv2.addWeighted(mask_blue, 1, mask_green, 1,0)
   temp2 = cv2.addWeighted(mask_yellow, 1, mask_red, 1,0)
   temp2 = cv2.addWeighted(temp2, 1, mask_purple, 1,0)
   mask_master = cv2.addWeighted(temp1, 1, temp2, 1,0)
   imS = cv2.resize(img, (960, 540))
   imM = cv2.resize(mask_master, (960, 540))

   threshold = 100
   ret,thresh = cv2.threshold(mask_master,250,255,cv2.THRESH_BINARY_INV)
   contours,hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
   canny_output = cv2.Canny(mask_master, threshold, threshold * 2)

   contours_poly = [None]*len(contours)
   boundRect = [None]*len(contours)
   centers = [None]*len(contours)
   radius = [None]*len(contours)
   for i, c in enumerate(contours):
      contours_poly[i] = cv2.approxPolyDP(c, 5, True)
      boundRect[i] = cv2.boundingRect(contours_poly[i])
      centers[i], radius[i] = cv2.minEnclosingCircle(contours_poly[i])

   drawing = np.zeros((canny_output.shape[0], canny_output.shape[1], 3), dtype=np.uint8)
   
   objects=[]

   hierarchy = hierarchy[0]
   for i in range(len(contours)):
      currentHierarchy = hierarchy[i]
      color = (rng.randint(0,256), rng.randint(0,256), rng.randint(0,256))
      if int(radius[i]) > 10 and int(radius[i]) < 200:
         cv2.circle(img, (int(centers[i][0]), int(centers[i][1])), int(radius[i]), color, 2)
         objects.append((int(centers[i][0]), int(centers[i][1]), int(radius[i])))
         

   

   # copy all masks to orignal image
   new_image = cv2.copyTo(img, mask_master)

   cv2.imshow("CV", mask_master)
   cv2.imshow('original', img)
   cv2.imshow('masked', new_image)

   while(True):
      k = cv2.waitKey(5) & 0xFF
      if k == 27:
         break

   cv2.destroyAllWindows()
   
   return

#imageAlter('RockPictures\\20200116_144936_flip.jpg')
imageAlter("RockPictures\\20200116_143420.jpg")
imageAnalyze("altered.jpg")