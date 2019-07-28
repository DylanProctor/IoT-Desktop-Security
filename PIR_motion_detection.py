import RPi.GPIO as GPIO
import sys
import time
import pubnub
from pubnub.pnconfiguration import PNConfiguration
from pubnub.pubnub import PubNub
from pubnub.callbacks import SubscribeCallback
from pubnub.enums import PNOperationType, PNStatusCategory

pnconfig = PNConfiguration()
pnconfig.subscribe_key = "sub-c-d11e8f9a-9871-11e9-8994-3e832ec25d8b"
pnconfig.publish_key = "pub-c-964c6e62-8094-417b-a4bd-979dd56a7d52"
pnconfig.ssl = False
pubnub = PubNub(pnconfig)


GPIO.setmode(GPIO.BCM)
#set the sensor to pin 23
pir = 23
GPIO.setup(pir, GPIO.IN)
flag = 0


class MySubscribeCallback(SubscribeCallback):
	def status(self, pubnub, status):
		pass
		
		if status.operation == PNOperationType.PNSubscribeOperation \
				or status.operation == PNOperationType.PNUnsubscribeOperation:
			if status.category == PNStatusCategory.PNConnectedCategory:
				pass

			elif status.category == PNStatusCategory.PNReconnectedCategory:
				pass

			elif status.category == PNStatusCategory.PNDisconnectedCategory:
				pass

			elif status.category == PNStatusCategory.PNUnexpectedDisconnectCategory:
				pass
			
			elif status.category == PNStatusCategory.PNAccessDeniedCategory:
				pass

			else:
				pass
		
		elif status.operation == PNOperationType.PNSubscribeOperation:
			if status.is_error():
				pass
			else:
				pass
		else:
			pass

	def presence(self, pubnub, presence):
		pass

	def message(self, pubnub, message):
		if message.message == 'ON':
			flag = 1
		elif message.message == 'OFF':
			flag = 0
		
pubnub.add_listener(MySubscribeCallback())
pubnub.subscribe().channels('Ch2').execute()

time.sleep(2)
while True:
	if flag = 1:
		if GPIO.input(pir):
			pubnub.publish().channel('Ch1').message("Intruder Detected!").async(publish_callback)
		print("Motion Detected")
		time.sleep(5)
	time.sleep(0.1)


GPIO.cleanup()