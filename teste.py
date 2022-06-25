import cv2
import uuid
import os
import time


cap = cv2.VideoCapture(0)
#width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
#height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

#while cap.isOpened(): 
ret, frame = cap.read()
    #image_np = np.array(frame)

cv2.imshow('frame', frame)
cv2.waitKey(2000)
time.sleep(10)