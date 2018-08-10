# -*- coding: utf-8 -*-
"""
Created on Fri Aug 10 23:12:39 2018

@author: Kushashwa Ravi Shrimali
"""
import cv2
import sys
import numpy as np

# read the video
cap = cv2.VideoCapture('animation.mp4')
if(cap.isOpened() == False):
    print("File path wrong.")
    sys.exit(0)

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        src = frame
        gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
         
        # blur the image
        blur = cv2.blur(gray, (3, 3))
        
        # binary thresholding of the image
        ret, thresh = cv2.threshold(blur, 150, 255, cv2.THRESH_BINARY)
        
        # find contours
        im2, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, \
                cv2.CHAIN_APPROX_SIMPLE)
        
        # create hull array for convexHull points
        hull = []
        
        # calculate points for each contour
        for i in range(len(contours)):
            hull.append(cv2.convexHull(contours[i], False))
        
        # create an empty black image
        drawing = np.zeros((thresh.shape[0], thresh.shape[1], 3), np.uint8)
        
        # draw contours and hull points
        for i in range(len(contours)):
            color_contours = (0, 255, 0) # color for contours
            color = (255, 255, 255) # color for convex hull
            # draw contours
            cv2.drawContours(drawing, contours, i, color_contours, 2, 8, hierarchy)
            # draw convex hull
            cv2.drawContours(drawing, hull, i, color, 2, 8)
        cv2.imshow("Frame", frame)
        cv2.imshow("Drawing", drawing)
        
        if cv2.waitKey(2) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()