print("Restarting the wifi module using the python library...")


from boltiot import Bolt
api_key = "XXXXXXXXXb-aaa7-4201162d906c"
device_id  = "BOLTXXXX703"
mybolt = Bolt(api_key, device_id)
response = mybolt.restart()
print (response, "\n")
