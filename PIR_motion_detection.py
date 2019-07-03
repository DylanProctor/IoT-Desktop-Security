import RPi.GPIO as GPIO
import picamera
import sys
import time

GPIO.setmode(GPIO.BCM)

outp = 23

GPIO.setup(outp, GPIO.IN)

camera = picamera.PiCamera()

time.sleep(2)
while True:
	if GPIO.input(outp):
		print("Motion Detected")
		camera.capture("intruder.jpg")
		time.sleep(3)
	time.sleep(0.1)


GPIO.cleanup()