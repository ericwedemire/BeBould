# Importing the necessary modules:

from skimage.feature import hog
from skimage.transform import pyramid_gaussian
from skimage.io import imread
from sklearn.externals import joblib
from sklearn.preprocessing import LabelEncoder
from sklearn.svm import LinearSVC, LinearSVR
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split
from skimage import color
from imutils.object_detection import non_max_suppression
import imutils
import numpy as np
import argparse
import cv2
import os
import glob
from PIL import Image # This will be used to read/modify images (can be done via OpenCV too)
from numpy import *

SIZES = [32, 64, 128]

for i in range(3):
    # define parameters of HOG feature extraction
    orientations = 9
    pixels_per_cell = (8, 8)
    cells_per_block = (2, 2)
    threshold = .3


    # define path to images:
    #pos_im_path = r"positives" # This is the path of our positive input dataset
    #neg_im_path= r"negatives"  # define the same for negatives


    # FOR WINDOWS
    pos_im_path = r"C:\Users\ericw\OneDrive\Desktop\GitHub\NotHackED2020\slidingWindow\positives" # This is the path of our positive input dataset
    neg_im_path = r"C:\Users\ericw\OneDrive\Desktop\GitHub\NotHackED2020\slidingWindow\negatives"  # define the same for negatives

    # read the image files:
    pos_im_listing = os.listdir(pos_im_path) # it will read all the files in the positive image path (so all the required images)
    neg_im_listing = os.listdir(neg_im_path)
    num_pos_samples = size(pos_im_listing) # simply states the total no. of images
    num_neg_samples = size(neg_im_listing)
    print()
    print(num_pos_samples) # prints the number value of the no.of samples in positive dataset
    print(num_neg_samples)
    data= []
    labels = []

    # compute HOG features and label them:
    for file in pos_im_listing: #this loop enables reading the files in the pos_im_listing variable one by one

        img = Image.open(pos_im_path + '/' + file) # open the file linux
        #img = Image.open(pos_im_path + '\\' + file) # open the file windows

        #img = img.resize((64,64))
        img = img.resize((SIZES[i],SIZES[i]))


        gray = img.convert('L') # convert the image into single channel i.e. RGB to grayscale
        ## i think she said to add color scale channels here if we wanted to, instead of the greyscale

        # calculate HOG for positive features
        fd = hog(gray, orientations, pixels_per_cell, cells_per_block, block_norm='L2', feature_vector=True) # fd= feature descriptor
        data.append(fd)
        labels.append(1)
        
    # Same for the negative images
    for file in neg_im_listing:

        img= Image.open(neg_im_path + '/' + file)   # linux
        #img= Image.open(neg_im_path + '\\' + file) # windows

        #img = img.resize((64,64))
        img = img.resize((SIZES[i],SIZES[i]))
        gray= img.convert('L')
        # Now we calculate the HOG for negative features
        fd = hog(gray, orientations, pixels_per_cell, cells_per_block, block_norm='L2', feature_vector=True) 
        data.append(fd)
        labels.append(0)

    # encode the labels, converting them from strings to integers
    le = LabelEncoder()
    labels = le.fit_transform(labels)

    # Partitioning the data into training and testing splits, using 80%
    # of the data for training and the remaining 20% for testing
    print(" Constructing training/testing split...")
    (trainData, testData, trainLabels, testLabels) = train_test_split(np.array(data), labels, test_size=0.20, random_state=42)

    #Train the linear SVM
    print(" Training Linear SVM classifier...")
    model = LinearSVC()
    model.fit(trainData, trainLabels)

    #Evaluate the classifier
    print(" Evaluating classifier on test data ...")
    predictions = model.predict(testData)
    print(classification_report(testLabels, predictions))

    # Save the model:
    #joblib.dump(model, 'rockModel.npy')
    modname = "rockModel-" + str(SIZES[i]) + ".npy"
    joblib.dump(model, modname)
