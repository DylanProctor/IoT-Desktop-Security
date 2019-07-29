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
        # The status object returned is always related to subscribe but could contain
        # information about subscribe, heartbeat, or errors
        # use the operationType to switch on different options
        if status.operation == PNOperationType.PNSubscribeOperation \
                or status.operation == PNOperationType.PNUnsubscribeOperation:
            if status.category == PNStatusCategory.PNConnectedCategory:
                pass
                # This is expected for a subscribe, this means there is no error or issue whatsoever
            elif status.category == PNStatusCategory.PNReconnectedCategory:
                pass
                # This usually occurs if subscribe temporarily fails but reconnects. This means
                # there was an error but there is no longer any issue
            elif status.category == PNStatusCategory.PNDisconnectedCategory:
                pass
                # This is the expected category for an unsubscribe. This means there
                # was no error in unsubscribing from everything
            elif status.category == PNStatusCategory.PNUnexpectedDisconnectCategory:
                pass
                # This is usually an issue with the internet connection, this is an error, handle
                # appropriately retry will be called automatically
            elif status.category == PNStatusCategory.PNAccessDeniedCategory:
                pass
                # This means that PAM does allow this client to subscribe to this
                # channel and channel group configuration. This is another explicit error
            else:
                pass
                # This is usually an issue with the internet connection, this is an error, handle appropriately
                # retry will be called automatically
        elif status.operation == PNOperationType.PNSubscribeOperation:
            # Heartbeat operations can in fact have errors, so it is important to check first for an error.
            # For more information on how to configure heartbeat notifications through the status
            # PNObjectEventListener callback, consult <link to the PNCONFIGURATION heartbeart config>
            if status.is_error():
                pass
                # There was an error with the heartbeat operation, handle here
            else:
                pass
                # Heartbeat operation was successful
        else:
            pass
            # Encountered unknown status type
 
    def presence(self, pubnub, presence):
        pass  # handle incoming presence data
 
    def message(self, pubnub, message):
		pass
        # if message.message == 'ON':
        # 	global flag
        # 	flag = 1
        # elif message.message == 'OFF':
		# 	global flag
		# 	flag = 0

pubnub.add_listener(MySubscribeCallback())
pubnub.subscribe().channels('Ch2').execute()

def publish_callback(result, status):
	pass

time.sleep(2)
while True:
	if GPIO.input(pir): #and flag == 1:
		pubnub.publish().channel('Ch1').message("Intruder Detected!").async(publish_callback)
		print("Motion Detected")
		time.sleep(5)
	time.sleep(0.1)


GPIO.cleanup()	