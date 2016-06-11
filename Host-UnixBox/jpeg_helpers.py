"""Methods for helping manipulate jpeg files

"""

import numpy as np
from PIL import Image
from subprocess import call


sys_call = ["ls", "-l"]
print sys_call
call(sys_call)

def ph():
  print('Hello world')

def open_jpeg(file_path):
  im = Image.open(file_path)
  print(im)
  im.show()
  return im
  
def get_rgb_ndarrays(im):
    ndarray = np.array(im)
    return ndarray

def get_exif(im):
  exif_data = im._getexif()
  return exif_data
