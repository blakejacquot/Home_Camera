"""Methods for helping manipulate jpeg files

"""

import cv2
import numpy as np
from PIL import Image

class Capture:
  """Object that contains metadata about the jpeg image at file_path
  as well as reduced data from red, blue, green channels.
  """
  def __init__(self, file_path):
    self.im = Image.open(file_path)
    self.im_shape = np.shape(self.im)
    self.rows = self.im_shape[0]
    self.cols = self.im_shape[1]
    self.exif_data = self.im._getexif()
    self.rgb = np.array(self.im)
    self.red = self.rgb[:,:,0]
    self.green = self.rgb[:,:,1]
    self.blue = self.rgb[:,:,2]
    
    self.red_dict = {}
    self.red_dict['quad0'] = self.red[0:self.rows/2 , 0:self.cols/2]
    self.red_dict['quad1'] = self.red[self.rows/2: , 0:self.cols/2]
    self.red_dict['quad2'] = self.red[0:self.rows/2 , self.cols/2:]
    self.red_dict['quad3'] = self.red[self.rows/2: , self.cols/2:]  
    self.red_dict['quad0_mean'] = np.mean(self.red_dict['quad0'])
    self.red_dict['quad1_mean'] = np.mean(self.red_dict['quad1'])
    self.red_dict['quad2_mean'] = np.mean(self.red_dict['quad2'])
    self.red_dict['quad3_mean'] = np.mean(self.red_dict['quad3'])

    self.green_items = {}
    self.green_items['quad1'] = self.green[0:self.rows/2 , 0:self.cols/2]
    self.green_items['quad2'] = self.green[self.rows/2: , 0:self.cols/2]
    self.green_items['quad3'] = self.green[0:self.rows/2 , self.cols/2:]
    self.green_items['quad4'] = self.green[self.rows/2: , self.cols/2:]

    self.blue_items = {}
    self.blue_items['quad1'] = self.blue[0:self.rows/2 , 0:self.cols/2]
    self.blue_items['quad2'] = self.blue[self.rows/2: , 0:self.cols/2]
    self.blue_items['quad3'] = self.blue[0:self.rows/2 , self.cols/2:]
    self.blue_items['quad4'] = self.blue[self.rows/2: , self.cols/2:]

def diffImg(t0, t1, t2):
  #http://www.steinm.com/blog/motion-detection-webcam-python-opencv-differential-images/  
  d1 = cv2.absdiff(t2, t1)
  d2 = cv2.absdiff(t1, t0)
  return cv2.bitwise_and(d1, d2)