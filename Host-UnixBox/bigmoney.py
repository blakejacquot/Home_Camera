"""Library of methods to detect change, flag interesting files, and copy
them to archive directory
"""

import jpeg_helpers as jp
import numpy as np
from subprocess import call
import cv2
import opencv_tools as cvt
import os
import matplotlib.pyplot as plt
import Image
from shutil import copyfile


def bigmoney(pic_dir):
  """Accepts path of jpeg files to reduce and returns lists of the paths 
  of files that may be intersting and their difference images with prior
  image
  """
  print('Processing files at ', pic_dir)


  files = []  
  for file in os.listdir(pic_dir):
    if file.endswith(".jpg"):
      files.append(file)
  
  #files = os.listdir(pic_dir) 
  
  
  files_full_path = []  
  for curr_file in files:
    files_full_path.append(os.path.join(pic_dir, curr_file))
  num_files = len(files)
  #num_files = 5
  files_with_change = [0]
  
  event_dir = os.path.join(pic_dir, 'Events')
  print os.path.isdir(event_dir)
  if os.path.isdir(event_dir):  
    pass
  else:    
    os.mkdir(event_dir)
  
  for i in range(1,num_files):
    collect_objects = []
    last_file_path = files_full_path[i-1]
    curr_file_path = files_full_path[i]
    last_collect = jp.Capture(last_file_path)
    curr_collect = jp.Capture(curr_file_path)
    collect_objects.append(last_collect)
    collect_objects.append(curr_collect)    
    files_with_change.append(is_event(collect_objects))  

  print files_with_change
  
  for i in range(len(files_with_change)):
    if files_with_change[i] == 1:
      print('Event')
#      copyfile(files_full_path[i], event_dir)
      sys_call = ["cp", files_full_path[i-1], event_dir]      
      call(sys_call)
      sys_call = ["cp", files_full_path[i], event_dir]
      call(sys_call)
#print np.sum(result)      
    else:
      pass
  
  return [], []
  

def is_event(collect_objects):
  """Assumes 2 Collect objects. Tests them for change and reports results
  0 if no change. 1 if change
  """
  norm_im = get_change_image(collect_objects)
  print norm_im.sum()
  if norm_im.sum() > 100000:
    return 1
    copyfile
  else:
    return 0   

def get_change_image(collect_objects):
  last_red = collect_objects[0].red  
  curr_red = collect_objects[1].red
  abs_diff_im = cvt.diff2Img(curr_red, last_red)
  #clip_diff = abs_diff_im.clip(99, 100)
  norm_im = abs_diff_im / curr_red
  return norm_im


      
    #diff_images.append(norm_image)    
    #for diff_image in diff_images:
    #        
      #fig = plt.figure()
      #plt.imshow(diff_image)  
  #plt.show()
  
#sys_call = ["ls", "-l"]
#call(sys_call)
#print np.sum(result)

def save_ndarray(array, save_full_path):
  im = Image.fromarray(array)
  im.save('test.png')
