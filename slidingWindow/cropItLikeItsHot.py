##
## Run like this:
## python3 cropItLikeItsHot.py --image newTestImage.jpg
##

import argparse
import cv2
from PIL import Image

# initialize the list of reference points and boolean indicating
# whether cropping is being performed or not
mouseX = 0
mouseY = 0
locations = []
cropping = False

# half the box crop size
size = 16

def click_and_crop(event, x, y, flags, param):
    # grab references to the global variables
    global mouseX, mouseY, cropping, locations

    # if the left mouse button was clicked, record the starting
    # (x, y) coordinates and indicate that cropping is being
    # performed
    if event == cv2.EVENT_LBUTTONDBLCLK:
        mouseX,mouseY = x,y
        locations.append((x,y))
        cropping = False

        # draw a rectangle around the region of interest
        cv2.rectangle(image, (mouseX-size, mouseY+size), (mouseX+size, mouseY-size), (0, 255, 0), 2)
        cv2.imshow("image", image)

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="RockPictures/")
args = vars(ap.parse_args())

# load the image, clone it, and setup the mouse callback function
image = cv2.imread(args["image"])
image = cv2.resize(image,(450,800))
clone = image.copy()
cv2.namedWindow("image")
cv2.setMouseCallback("image", click_and_crop)

# keep looping until the 'q' key is pressed
while True:
    # display the image and wait for a keypress
    cv2.imshow("image", image)
    key = cv2.waitKey(1) & 0xFF
    # if the 'r' key is pressed, reset the cropping region
    if key == ord("r"):
        image = clone.copy()
    # save cropped images
    elif key == ord("s"):
        print(locations)
        for i,centerpoint in enumerate(locations):
            crop = image[centerpoint[1]-size:centerpoint[1]+size, centerpoint[0]-size:centerpoint[0]+size]
            cv2.imwrite(str(i)+'.png', crop)
        break
    # if the 'c' key is pressed, break from the loop
    elif key == ord("c"):
        break



# close all open windows
cv2.destroyAllWindows()