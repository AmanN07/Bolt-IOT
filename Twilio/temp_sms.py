# Working perfectly fine

import conf, json, time
from boltiot import Sms, Bolt 

maximum_limit = 600
minimum_limit = 360



mybolt = Bolt(conf.API_KEY, conf.DEVICE_ID)
sms = Sms(conf.SID, conf.AUTH_TOKEN, conf.TO_NUMBER, conf.FROM_NUMBER)

def temp_sensor():
    total = 8 
    while total > 0: 
        print ("Reading sensor value")
        response = mybolt.analogRead('A0') 
        data = json.loads(response) 
        print("Sensor value is: " + str(data['value']))
        try: 
            sensor_value = int(data['value']) 
            if sensor_value > maximum_limit or sensor_value < minimum_limit:
                print("Making request to Twilio to send a SMS")
                response = sms.send_sms("The Current temperature sensor value is " +str(sensor_value))
                print("Response received from Twilio is: " + str(response))
                print("Status of SMS at Twilio is :" + str(response.status))
        except Exception as e: 
            print ("Error occured: Below are the details")
            print (e)
        time.sleep(10)
        total = total - 1

while True:
    temp_sensor()
    time.sleep(5)