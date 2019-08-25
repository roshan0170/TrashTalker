from boltiot import Bolt, Sms #Import Sms and Bolt class from boltiot library
import json, time

garbage_full_limit = 5 # the distance between device and  garbage in dustbin in cm

API_KEY = "bef30cf7-8bb7-4075-907a-8743b6d3c457"
DEVICE_ID  = "BOLT1235593"

SID = 'ACf9b68501dd4c43c099896dc8359f8ffe'
AUTH_TOKEN = '0d3334403f76fe4ea734fe5862a2e263'
FROM_NUMBER = '3344871148'
TO_NUMBER = '+917034645542'

mybolt = Bolt(API_KEY, DEVICE_ID) #Create object to fetch data
sms = Sms(SID, AUTH_TOKEN, TO_NUMBER, FROM_NUMBER) #Create object to send SMS
response = mybolt.serialRead('10')
print response

while True:
    response = mybolt.serialRead('10')  #Fetching the value from Arduino
    data = json.loads(response)
    garbage_value = data['value'].rstrip()
    print "Garbage level is", garbage_value
    if int(garbage_value) < garbage_full_limit:
        response = sms.send_sms('Hello Sir, I am full-Please do the needful, Trash Talker')
    time.sleep(200)

