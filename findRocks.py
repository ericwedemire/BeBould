import cv2
import numpy as np
import imutils
import random as rng

img = cv2.imread('RockPictures/20200116_144936.jpg')
cv2.namedWindow("original", cv2.WINDOW_NORMAL)
cv2.namedWindow("CV", cv2.WINDOW_NORMAL)
cv2.namedWindow("Edge", cv2.WINDOW_NORMAL)
cv2.namedWindow("Boxes", cv2.WINDOW_NORMAL)

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

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
edgeMap = imutils.auto_canny(mask)
threshold = 100
ret,thresh = cv2.threshold(mask,250,255,cv2.THRESH_BINARY_INV)
contours,hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
canny_output = cv2.Canny(mask, threshold, threshold * 2)
# _, contours = cv2.findContours(canny_output, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

contours_poly = [None]*len(contours)
boundRect = [None]*len(contours)
centers = [None]*len(contours)
radius = [None]*len(contours)
for i, c in enumerate(contours):
    contours_poly[i] = cv2.approxPolyDP(c, 5, True)
    boundRect[i] = cv2.boundingRect(contours_poly[i])
    centers[i], radius[i] = cv2.minEnclosingCircle(contours_poly[i])

drawing = np.zeros((canny_output.shape[0], canny_output.shape[1], 3), dtype=np.uint8)
    
hierarchy = hierarchy[0]
for i in range(len(contours)):
    currentHierarchy = hierarchy[i]
    color = (rng.randint(0,256), rng.randint(0,256), rng.randint(0,256))
    #cv2.drawContours(drawing, contours_poly, i, color)
    
    if int(radius[i]) > 12:
        cv2.circle(drawing, (int(centers[i][0]), int(centers[i][1])), int(radius[i]), color, 2)
    

imS = cv2.resize(img, (960, 540))
imM = cv2.resize(mask, (960, 540))
imE = cv2.resize(edgeMap, (960, 540))
imB = cv2.resize(drawing, (960, 540))

cv2.imshow('original', img)
cv2.imshow('CV', mask)
cv2.imshow('Edge', edgeMap)
cv2.imshow('Boxes', drawing)

while(True):
   k = cv2.waitKey(5) & 0xFF
   if k == 27:
      break

cv2.destroyAllWindows()