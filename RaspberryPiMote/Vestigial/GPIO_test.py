import RPi.GPIO as GPIO
import time

pwmPin = 18

GPIO.setmode(GPIO.BCM)
GPIO.setup(pwmPin, GPIO.OUT)

GPIO.output(pwmPin, GPIO.HIGH)