print("Checking the status of the BOLT wifi module..... \n")


from boltiot import Bolt
api_key = "XXXXXXXXXXX-4e6b-aaa7-4201162d906c"
device_id  = "BOLTXXXX703"
mybolt = Bolt(api_key, device_id)
response = mybolt.isOnline()
print (response, "\n")

