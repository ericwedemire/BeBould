#!/usr/bin/env python3

import cv2
import numpy as np
import imutils
import PIL

def imageAlter(image):
   alteredImage = PIL.Image.open(image)


   return alteredImage

def imageAnalyze(image):
   img = cv2.imread(image)
   cv2.namedWindow("original", cv2.WINDOW_NORMAL)
   cv2.namedWindow("CV", cv2.WINDOW_NORMAL)

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
   #-----------

   mask = cv2.inRange(hsv, blue_lower,blue_upper)
   imS = cv2.resize(img, (960, 540))
   imM = cv2.resize(mask, (960, 540))

   cv2.imshow('original', img)
   cv2.imshow('CV', mask)

   while(True):
      k = cv2.waitKey(5) & 0xFF
      if k == 27:
         break

   cv2.destroyAllWindows()

   return

try:
   # For filthy Windows users
   imageAnalyze('RockPictures\\20200116_144936.jpg')
except:
   # FOr everyone else
   imageAnalyze('RockPictures/20200116_144936.jpg')