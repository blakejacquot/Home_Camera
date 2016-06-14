"""Starts all host-PC image processing and logging
Assumes jpg files exist in pic_dir. Compares them for changes

Inputs: None
Outputs: None
"""

import jpeg_helpers as jp
import numpy as np
from subprocess import call
import os
import matplotlib.pyplot as plt
import bigmoney

pic_dir = "/home/blakejacquot/Desktop/pics"

#sys_call = ["ls", "-l"]
#print sys_call
#call(sys_call)
#jp.detect_red_change(im4, im5)
#imshow(im4.red_dict['quad1'])
#result = jp.diffImg(im4.red, im5.red, im6.red)  
#imshow(result)
#print np.sum(im4.red)
#print np.sum(result)
#print np.sum(result)
  
files = os.listdir(pic_dir)
collects = []

for file in files:
  file_path = os.path.join(pic_dir, file)
  collects.append(jp.Capture(file_path))

diff_images = []  
for i in range(1,len(collects)-1):
  prior_cap = collects[i-1]  
  curr_cap = collects[i]
  next_cap = collects[i+1]  
  diff_result = jp.diffImg(prior_cap.red, curr_cap.red, next_cap.red)
  diff_images.append(diff_result)  
  if np.sum(diff_result) > 5000000:
    disp ('Change Detected')

print(len(diff_images))
for diff_image in diff_images:
  fig = plt.figure()
  imshow(diff_image

#plt_subplot(241)
#plt.imshow