import cv2
import numpy as np
import imutils

print("test")
img = cv2.imread('RockPictures\\20200116_144936.jpg')
cv2.namedWindow("original", cv2.WINDOW_NORMAL)
cv2.namedWindow("CV", cv2.WINDOW_NORMAL)

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

lower_range = np.array([110,50,50])
upper_range = np.array([130,255,255])

mask = cv2.inRange(hsv, lower_range, upper_range)
imS = cv2.resize(img, (960, 540))
imM = cv2.resize(mask, (960, 540))

cv2.imshow('original', img)
cv2.imshow('CV', mask)

while(True):
   k = cv2.waitKey(5) & 0xFF
   if k == 27:
      break

cv2.destroyAllWindows()