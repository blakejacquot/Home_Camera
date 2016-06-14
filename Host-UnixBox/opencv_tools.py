"""
Opencv_tools contains wrappers and helper functions for making
opencv calls
"""

import cv2

def diffImg(t0, t1, t2):
  #http://www.steinm.com/blog/motion-detection-webcam-python-opencv-differential-images/  
  d1 = cv2.absdiff(t1, t0)
  d2 = cv2.absdiff(t2, t0)
  return cv2.bitwise_and(d1, d2)
  #return d1
  
def diff2Img(t0, t1):
  diff = cv2.absdiff(t1, t0)
  return diff