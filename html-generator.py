"""Scans destination directory for .jpg files and generates index.html page with image and timestamp"""

import os
import time

destination_directory = ("/var/www/html")

while True:
  print "hello world"
  print os.listdir(destination_directory)
  time.sleep(3)
