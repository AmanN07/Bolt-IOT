import json, time                 # importing libraries
from boltiot import Bolt

# api_key and device_id of the Bolt Wi-Fi module
bolt_api_key = '6d84b61e-c5ae-4e6b-aaa7-4201162d906c'   
device_id = 'BOLT5436703'                 

nbolt = Bolt(bolt_api_key, device_id)

# defining the function to produce sound in buzzer
def noise_maker(pin, value):
	response = nbolt.analogWrite(pin, value)
	print (response)

# creating the infinte loop so that program can run until we press 'ctrl+c' 
while True:
	response = nbolt.analogRead('A0')
	data = json.loads(response)
	try:
		intensity = int(data['value'])
		intensity = int(intensity/4 - 1)  #converting the input(0 to 1023) to output(0 to 255)
		
		print ("Light intensity is ",intensity)
		noise_maker('0', intensity)   # calling function noise_maker
		
		time.sleep(5)         # buzz for 3 sec
		noise_maker('0', 0)  # switching off buzzer
	except Exception as e:
		print ("Error ", e)
	time.sleep(10)          # receiving the input from LDR after every 10 sec

	