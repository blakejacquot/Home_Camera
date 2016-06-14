"""Library of methods to detect change, flag interesting files, and copy
them to archive directory
"""

import jpeg_helpers as jp
import numpy as np
#from subprocess import call
import cv2
import opencv_tools as cvt
import os
import matplotlib.pyplot as plt
import Image


def bigmoney(pic_dir):
  """Accepts path of jpeg files to reduce and returns lists of the paths 
  of files that may be intersting and their difference images with prior
  image
  """
  print('Processing files at ', pic_dir)
  collects = [] 
  files = os.listdir(pic_dir)    
  for i in range(3):
    file_path = os.path.join(pic_dir, files[i])
    print('Processing = ', files[i])
    collects.append(jp.Capture(file_path))

  diff_images = []  
  for j in range(2,3):
    last_last_red = collects[j-2].red    
    last_red = collects[j-1].red
    curr_red = collects[j].red
    abs_diff_im = cvt.diff2Img(curr_red, last_red)
    #clip_diff = abs_diff_im.clip(99, 100)
    div_im = abs_diff_im / curr_red    
    print np.max(div_im)
    print np.mean(div_im)
    print np.sum(div_im)    
    diff_images.append(div_im)    
    for diff_image in diff_images:
      fig = plt.figure()
      plt.imshow(diff_image)  
  plt.show()
 
  save_ndarray(diff_image, 1) 
 
  return [], []
  

def get_change_images():
  pass
#sys_call = ["ls", "-l"]
#call(sys_call)
#print np.sum(result)

def save_ndarray(array, save_full_path):
  im = Image.fromarray(array)
  im.save('test.png')
