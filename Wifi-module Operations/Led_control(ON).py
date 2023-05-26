print("Controlling the led light using python library....")


from boltiot import Bolt
api_key = "6d84b61e-c5ae-4e6b-aaa7-4201162d906c"
device_id  = "BOLT5436703"
mybolt = Bolt(api_key, device_id)
response = mybolt.digitalWrite('0', 'HIGH')
print (response, "\n")

