from boltiot import Bolt, Sms #Import Sms and Bolt class from boltiot library
import json, time, datetime
import conf


bolt = Bolt(conf.API_KEY, conf.DEVICE_ID)
sms = Sms(conf.SID, conf.AUTH_TOKEN, conf.TO_NUMBER, conf.FROM_NUMBER)
while True:
    data = json.loads(bolt.serialRead('10'))['value'] #read the value sent from arduino
    print(data) 
    try:
        print("Sending message...")
        response = sms.send_sms(data)
        time.sleep(10)
    except Exception as e:
        print("Error occurred: Below are the details")
        print(e)
    time.sleep(10)
