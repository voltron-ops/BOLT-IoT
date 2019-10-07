from boltiot import Bolt
api_key = "Your Bolt API Key"
device_id  = "BOLT Device ID"
mybolt = Bolt(api_key, device_id)
response = mybolt.isOnline()
print(response)
