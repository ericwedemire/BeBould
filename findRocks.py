import cv2
import numpy as np

print("test")

img = cv2.imread('../IMG.jpg')

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
   blue_lower = np.array([115,161,221])
   blue_upper = np.array([36,52,77])
   #-----------

# Background Colors To Avoid (Gray/Pink wall)
   #-----------

   #defining the Range of Gray Wall
   gray_lower = np.array([183,179,178])
   gray_upper = np.array([103,102,100])

   #defining the Range of Pink Wall
   pink_lower = np.array([223,164,196])
   pink_upper = np.array([162,177,110])
   #-----------

mask = cv2.inRange(hsv, lower_range, upper_range)

cv2.imshow('image', img)
cv2.imshow('mask', mask)

while(True):
   k = cv2.waitKey(5) & 0xFF
   if k == 27:
      break

cv2.destroyAllWindows()
