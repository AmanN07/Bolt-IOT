print("Controlling the led light using python library....")


from boltiot import Bolt
api_key = "XXXXXXXXXXXX-4e6b-aaa7-4201162d906c"
device_id  = "BOLTXXXX703"
mybolt = Bolt(api_key, device_id)
response = mybolt.digitalWrite('0', 'LOW')
print(response, "\n")
