import tweepy
import tweepy2
import json, time
from boltiot import Bolt

    # Dictionary to store credentials as key-value pairs.
config = {
"consumer_key"        : tweepy2.consumer_key,
"consumer_secret"     : tweepy2.consumer_secret,
"access_token"        : tweepy2.access_token,
"access_token_secret" : tweepy2.access_token_secret
}

# Method to authenticate user via Tweepy and return API object
def get_api_object(cfg):
    auth =tweepy.OAuthHandler(cfg['consumer_key'],
                                  cfg['consumer_secret'])
    auth.set_access_token(cfg['access_token'],
                              cfg['access_token_secret'])
    return tweepy.API(auth)

mybolt = Bolt(tweepy2.bolt_cloud_api_key, tweepy2.device_id)
temperature_threshold = 59
while True:
    response = mybolt.analogRead('A0')
    data = json.loads(response)
    print (data['value'])
    try:
        sensor_value = int(data['value'])
        if sensor_value > temperature_threshold:
            print "Temperature has crossed the threshold."
            # Call get_api_object to authenticate user and get the API object
            api_object = get_api_object(config)
            # Store the tweet message in the variable
            tweet = "Temperature has crossed the threshold."
            # Post the tweet on your Twitter account using the update_status method.
            status = api_object.update_status(status=tweet)
    except Exception as e:
        print ("An error occurred ", e)
    time.sleep(10)
