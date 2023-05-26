print("Checking the status of the BOLT wifi module..... \n")
from boltiot import Bolt
api_key = "6d84b61e-c5ae-4e6b-aaa7-4201162d906c"
device_id  = "BOLT5436703"
mybolt = Bolt(api_key, device_id)
response = mybolt.isOnline()
print (response, "\n")


# print("Restarting the wifi module using the python library...")

# from boltiot import Bolt
# api_key = "6d84b61e-c5ae-4e6b-aaa7-4201162d906c"
# device_id  = "BOLT5436703"
# mybolt = Bolt(api_key, device_id)
# response = mybolt.restart()
# print (response, "\n")


# print("Controlling the led light using python library....")

# from boltiot import Bolt
# api_key = "6d84b61e-c5ae-4e6b-aaa7-4201162d906c"
# device_id  = "BOLT5436703"
# mybolt = Bolt(api_key, device_id)
# response = mybolt.digitalWrite('0', 'HIGH')
# print (response, "\n")

