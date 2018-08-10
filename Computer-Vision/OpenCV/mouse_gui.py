# -*- coding: utf-8 -*-
"""
Created on Fri Aug 10 23:18:35 2018

@author: Saurabh
"""
import cv2
import sys
import numpy as np

mouseX = 0
mouseY = 0

def callback_mouse(event, x, y, flags, param):
    global mouseX, mouseY
    if event == cv2.EVENT_LBUTTONDBLCLK:
        mouseX, mouseY = x, y
    
cv2.namedWindow("Frame")
cv2.setMouseCallback("Frame", callback_mouse)

# read the video
cap = cv2.VideoCapture('animation.mp4')

if(cap.isOpened() == False):
    print("File path wrong.")
    sys.exit(0)

while(cap.isOpened()):
    ret, frame = cap.read()
    src = frame
    gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
        
    cv2.imshow("Frame", gray)
    print(gray[497][259])
    k = cv2.waitKey(20) & 0xFF
    if k == 27:
        break
    elif k == ord('a'):
        print(mouseX, mouseY)

cap.release()
cv2.destroyAllWindows()