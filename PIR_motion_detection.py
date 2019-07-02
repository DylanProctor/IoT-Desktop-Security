import RPi.GPIO as GPIO
import sys
import time

GPIO.setmode(GPIO.BCM)

outp = 23

GPIO.setup(outp, GPIO.IN)


try:
	time.sleep(2)
	while True:
		if GPIO.input(outp):
			print("Motion Detected")
			time.sleep(2)
		time.sleep(0.1)
except:
	GPIO.cleanup()
