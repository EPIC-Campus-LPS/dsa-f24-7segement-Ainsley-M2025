import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

i = 4

for i in range (27):
   GPIO.setup(i, GPIO.OUT)
   GPIO.output (i, GPIO.LOW)
