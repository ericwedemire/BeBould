##
## Run like this:
## python3 cropItLikeItsHot.py --image newTestImage.jpg
##

import argparse
import cv2

# initialize the list of reference points and boolean indicating
# whether cropping is being performed or not
mouseX,mouseY = 0,0
cropping = False

def click_and_crop(event, x, y, flags, param):
	# grab references to the global variables
	global mouseX, mouseY, cropping

	# if the left mouse button was clicked, record the starting
	# (x, y) coordinates and indicate that cropping is being
	# performed
	if event == cv2.EVENT_LBUTTONDBLCLK:
		mouseX,mouseY = x,y
		cropping = False

		# draw a rectangle around the region of interest
		cv2.rectangle(image, (mouseX-16, mouseY+16), (mouseX+16, mouseY-16), (0, 255, 0), 2)
		cv2.imshow("image", image)



# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="/")
args = vars(ap.parse_args())

# load the image, clone it, and setup the mouse callback function
image = cv2.imread(args["image"])
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
	# if the 'c' key is pressed, break from the loop
	elif key == ord("c"):
		break

# if there are two reference points, then crop the region of interest
# from teh image and display it
if mouseX != 0 and mouseY != 0:
	roi = clone[mouseX-16:mouseY+16, mouseX+16:mouseY-16]
	cv2.imshow("ROI", roi)
	cv2.waitKey(0)
# close all open windows
cv2.destroyAllWindows()


# close all open windows
cv2.destroyAllWindows()