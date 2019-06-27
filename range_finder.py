import sys
import time
import RPi.GPIO as GPIO 
from python import pubnub
from pubnub.pnconfiguration import PNConfiguration
from pubnub.pubnub import PubNub
from pubnub.callbacks import SubscribeCallback
from pubnub.enums import PNOperationType, PNStatusCategory

GPIO.setmode(GPIO.BCM)

TRIG = 20
ECHO = 26

print("Measuring distance")

GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

GPIO.output(TRIG, False)
print("Waiting for measurement")
time.sleep(2)

GPIO.output(TRIG, True)
time.sleep(0.00001)
GPIO.output(TRIG, False)

while GPIO.input(ECHO) == 0:
	pulse_start = time.time()

while GPIO.input(ECHO) == 1:
	pulse_end = time.time()

pulse_time = pulse_end - pulse_start

distance = pulse_time * 17150
distance = round(distance, 2)

print("DIstance: ", distance, "cm")

GPIO.cleanup()