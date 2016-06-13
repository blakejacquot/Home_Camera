"""Starts all host-PC image processing and logging
Assumes jpg files exist in ~/Desktop/pics

Inputs: None
Outputs: None
"""

import jpeg_helpers as jp
import numpy as np
from subprocess import call

#sys_call = ["ls", "-l"]
#print sys_call
#call(sys_call)

file_to_open4 = '/home/blakejacquot/Desktop/pics/image4.jpg'
file_to_open5 = '/home/blakejacquot/Desktop/pics/image5.jpg'
file_to_open6 = '/home/blakejacquot/Desktop/pics/image6.jpg'

im4 = jp.Capture(file_to_open4)
im5 = jp.Capture(file_to_open5)
im6 = jp.Capture(file_to_open6)

jp.detect_red_change(im4, im5)

imshow(im4.red_dict['quad1'])

result = jp.diffImg(im4.red, im5.red, im6.red)
  
imshow(result)


print np.sum(im4.red)
print np.sum(result)

print np.sum(result)

if np.sum(result) > 5000000:
  disp ('Change Detected')