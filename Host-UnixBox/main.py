"""Starts all host-PC image processing and logging
Assumes jpg files exist in pic_dir. Compares them for changes

Inputs: None
Outputs: None
"""
#import jpeg_helpers as jp
#import numpy as np
#from subprocess import call
import bigmoney

pic_dir = "/home/blakejacquot/Desktop/pics"
  
interesting_images, diff_images = bigmoney.bigmoney(pic_dir)