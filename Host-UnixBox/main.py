"""Starts all host-PC image processing and logging
Assumes jpg files exist in ~/Desktop/pics

Inputs: None
Outputs: None
"""

import jpeg_helpers as jp
import numpy as np

file_to_open4 = '/home/blakejacquot/Desktop/pics/image4.jpg'
file_to_open5 = '/home/blakejacquot/Desktop/pics/image5.jpg'
file_to_open6 = '/home/blakejacquot/Desktop/pics/image6.jpg'

im4 = jp.open_jpeg(file_to_open4)
im5 = jp.open_jpeg(file_to_open5)
im6 = jp.open_jpeg(file_to_open6)


rgb4 = jp.get_rgb_ndarrays(im4)
rgb5 = jp.get_rgb_ndarrays(im5)
rgb6 = jp.get_rgb_ndarrays(im6)

diff0 = abs(rgb4[:,:,0] - rgb5[:,:,0])
diff1 = abs(rgb4[:,:,1] - rgb5[:,:,1])
diff2 = abs(rgb4[:,:,2] - rgb5[:,:,2])

#imshow(rgb4)

rgb_diff = rgb4
rgb_diff[:,:,0] = diff0
rgb_diff[:,:,1] = diff1
rgb_diff[:,:,2] = diff2

imshow(rgb_diff)

print type(diff0)
print shape(diff0)
print np.mean(diff0)

#imshow(diff0)

#imshow(rgb4[:,:,0] - rgb5[:,:,0])

#imshow(np.asarray(im))
#imshow(rgbarray[:,:,1])