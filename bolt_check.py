from boltiot import Bolt
api_key = "Your Bolt API Key"
device_id  = "BOLT Device ID"
mybolt = Bolt(api_key, device_id)
#response = mybolt.restart()
response = mybolt.isOnline()
#response = mybolt.analogWrite('0', '10')
print (response)
