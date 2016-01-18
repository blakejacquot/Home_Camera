#import RPi.GPIO as GPIO
#import array
#import bitstring
import serial
import sys
import time
 

print(sys.version_info)

ser = serial.Serial("/dev/ttyUSB0") #open port
ser.baudrate = 38400
ser.close()
ser.timeout = 1
ser.open()

#hex_string = "56002600"
#hex_data = hex_string.decode("hex")
#print hex_data
##array.array('B', hex_data)
#command = bytearray(hex_data)
#num_bytes_written = ser.write(command)
#print num_bytes_written
#data = ser.read(4)
#print data
#ser.close()
#
#
#decode_data = hex_data.decode()
#print hex_data
#

i = 3
while i>0:
    command = bytearray.fromhex('56 00 36 01 00')
    print('The byte array version is = ')
    print(command)
    print('Transmitted data')
    for d in command:
        print(hex(d))
    print(type(command))
    num_bytes_written = ser.write(command)
    
    print('Number of bytes written = ',num_bytes_written)

    time.sleep(0)    
    
    data = ser.read()
    print('Number of bytes read = ',len(data))
    print(data)
    print(type(data)) 
    data = bytearray(data)
    print('Received data')
    for d in data:
        print(hex(d))
        #print(hex(d))
    #    print(hex(d))
    i = i-1

ser.close() 

ser.open()
command = bytearray.fromhex('56 00 26 01')
ser.write(command)
resp = ''
time.sleep(1)
while (ser.inWaiting() > 0):
    data = ser.read()
    resp += data

print resp
for d in resp:
    print(hex(d))

