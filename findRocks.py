import cv2
import numpy as np
import imutils
import random as rng
import math

def mouse_drawing(event, x, y, flags, params):
    if event == cv2.EVENT_LBUTTONDOWN:
        for hold in objects:
            x2 = hold[0]
            y2 = hold[1]
            rad = hold[2]
            dist = math.sqrt((x2 - x)**2 + (y2 - y)**2)
            font = cv2.FONT_HERSHEY_SIMPLEX
            if (dist < rad):
                cv2.putText(img,"HERE",(x,y), font, .5,(255,255,255),2,cv2.LINE_AA)
                cv2.imshow('original', img)
                print(dist)
        print("Left click", x, y)

img = cv2.imread('RockPictures/20200116_144936_flip.jpg')
cv2.namedWindow("original", cv2.WINDOW_NORMAL)
cv2.namedWindow("CV", cv2.WINDOW_NORMAL)
blur = cv2.blur(img,(5,5))
hsv = cv2.cvtColor(blur, cv2.COLOR_BGR2HSV)

objects = []

# Accepted Colors
#-----------
#defining the Range of ??? color
lower_range = np.array([50,50,50])
upper_range = np.array([200,200,200])

lower_blue = np.array([240,240,240])
upper_blue = np.array([255,255,255])

mask = cv2.inRange(hsv, lower_range, upper_range)

mask = cv2.inRange(hsv, lower_blue, upper_blue)

threshold = 100
ret,thresh = cv2.threshold(mask,250,255,cv2.THRESH_BINARY_INV)
contours,hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
canny_output = cv2.Canny(mask, threshold, threshold * 2)

contours_poly = [None]*len(contours)
boundRect = [None]*len(contours)
centers = [None]*len(contours)
radius = [None]*len(contours)
for i, c in enumerate(contours):
    contours_poly[i] = cv2.approxPolyDP(c, 5, True)
    boundRect[i] = cv2.boundingRect(contours_poly[i])
    centers[i], radius[i] = cv2.minEnclosingCircle(contours_poly[i])

drawing = np.zeros((canny_output.shape[0], canny_output.shape[1], 3), dtype=np.uint8)
    

tempStore = []
for i in range(len(contours)):
    color = (rng.randint(0,256), rng.randint(0,256), rng.randint(0,256))
    if int(radius[i]) > 10 and int(radius[i]) < 200:
        #cv2.circle(img, (int(centers[i][0]), int(centers[i][1])), int(radius[i]), color, 2)
        tempStore.append((int(centers[i][0]), int(centers[i][1]), int(radius[i])))
        
tempStore.sort(key=lambda x: x[2],reverse=True)
for i in range(len(tempStore)):
    color = (rng.randint(0,256), rng.randint(0,256), rng.randint(0,256))
    flag = 0
    for x in range(len(tempStore)):
        dist = math.sqrt((tempStore[i][0] - tempStore[x][0])**2 + (tempStore[i][1] - tempStore[x][1])**2)
        if dist < tempStore[x][2] and i != x:
            flag = 1
    if not flag:
        cv2.circle(img, (tempStore[i][0], tempStore[i][1]), tempStore[i][2], color, 2)   
        objects.append((tempStore[i][0], tempStore[i][1], tempStore[i][2]))    


imS = cv2.resize(img, (960, 540))
imM = cv2.resize(mask, (960, 540))

cv2.imshow('original', img)
cv2.imshow('CV', mask)
cv2.setMouseCallback('original', mouse_drawing)
print(len(objects))
while(True):
   k = cv2.waitKey(5) & 0xFF
   if k == 27:
      break

cv2.destroyAllWindows()