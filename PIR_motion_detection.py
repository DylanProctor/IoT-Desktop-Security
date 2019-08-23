import RPi.GPIO as GPIO
import sys
import time
import pubnub
from pubnub.pnconfiguration import PNConfiguration
from pubnub.pubnub import PubNub
from pubnub.callbacks import SubscribeCallback
from pubnub.enums import PNOperationType, PNStatusCategory

pnconfig = PNConfiguration()
pnconfig.subscribe_key = "SUBSCRIBE_KEY"
pnconfig.publish_key = "PUBLISH_KEY"
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
		if status.operation == PNOperationType.PNSetStateOperation \
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
		global flag
		if message.message == 'ON':
			flag = 1
		elif message.message == 'OFF':
			flag = 0

pubnub.add_listener(MySubscribeCallback())
pubnub.subscribe().channels('Ch2').execute()

def publish_callback(result, status):
	pass

time.sleep(2)
while True:
	if GPIO.input(pir) and flag == 1:
		pubnub.publish().channel('Ch1').message("Intruder Detected!").pn_async(publish_callback)
		print("Motion Detected")
		time.sleep(5)
	time.sleep(0.1)


GPIO.cleanup()	
