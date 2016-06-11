print('Hello World')

from subprocess import call
call(["ls", "-l"])
sys_call = "fswebcam -r 640x480 test.jpg -s 2"
sys_call = ["ls", "-l"]
sys_call = ["fswebcam", "-r", "640x480", "test.jpg", "-s", "2"]
print(sys_call)

#call(["fswebcam -r 640x480 test.jpg -s 2"])
call(sys_call)

