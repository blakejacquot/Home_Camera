"""Scans destination directory for .jpg files and generates index.html page with image and timestamp"""

import os
import time

destination_directory = ("/var/www/html")
os.chdir(destination_directory)

while True:
  jpg_list = []
  print "hello world"
  dest_dir_contents = os.listdir(destination_directory)
  for file in dest_dir_contents:
    if file.endswith(".jpg"):
      print file
      jpg_list.append(file)
  print jpg_list

  html_file = open("pics.html", "w")
  html_file.write("<html>\n")
  html_file.write("Hello world. Goodbye kitty<br>\n")
  for file in jpg_list:
    html_file.write("Current file = " + file + "<br>\n")
    html_file.write('<img src="' + file + '" alt="Nothing" width="104" height="142">')

  html_file.write("</html>\n")
  html_file.close()
  

  time.sleep(3)
