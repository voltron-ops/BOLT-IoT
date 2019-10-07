import conf
from boltiot import Sms, Bolt , Email
import json, time

minimum_limit = 300 
maximum_limit = 600  


mybolt = Bolt(conf.API_KEY, conf.DEVICE_ID)
sms = Sms(conf.SSID, conf.AUTH_TOKEN, conf.TO_NUMBER, conf.FROM_NUMBER)
mailer = Email(conf.MAILGUN_API_KEY, conf.SANDBOX_URL,conf.SENDER_EMAIL,conf.RECIPIENT_EMAIL)

while True: 
    response = mybolt.analogRead('A0') 
    data = json.loads(response) 
    print (data['value'])
    try: 
        sensor_value = int(data['value']) 
        print (sensor_value)
        if sensor_value > maximum_limit or sensor_value < minimum_limit:
            response = sms.send_sms("The Current temperature sensor value is " +str(sensor_value))
            response = mailer.send_email("Alert", "The Current temperature sensor value is " +str(sensor_value)) 
    except Exception as e: 
        print ("Error",e)
    time.sleep(10)
