import os
import requests
import array
import json
import datetime 

from dotenv import load_dotenv
load_dotenv()


API_KEY = os.getenv('ARKESEL_API_KEY')


class APIKeyMissingError(Exception):
    pass

if API_KEY is None:
    raise APIKeyMissingError(
        "All methods require an API key. See "
        "https://sms.arkesel.com/user/sms-api/info "
        "for how to retrieve an API key from Arkesel "
    )


session = requests.Session()
session.params = {}
session.params['api_key'] = API_KEY

class ArkeselSMS(object):
    def __init__(self) :
        # self.message_id = message_id
        # self.recipients = array.array(recipients)
        pass
    
    def sendSms(sender:str, message: str, recipients: array.array ):
        header = {"api-key":API_KEY , 'Content-Type': 'application/json', 'Accept':'application/json'}
        SEND_SMS_URL = "https://sms.arkesel.com/api/v2/sms/send"

        payload ={
            "sender":sender,
            "message":message,
            "recipients": recipients 
        }

        response = requests.post(SEND_SMS_URL, headers=header,json=payload)
        print (response.text.encode('utf8'))
        # print(response.status_code)
    # sendSms('Trial','just trying this',['233248649732'])

    
    
    
    
    
    def scheduledSms(sender:str,message:str,recipients:array.array,scheduled_date:str):
        header = {"api-key":API_KEY , 'Content-Type': 'application/json', 'Accept':'application/json'}
        SEND_SMS_URL = "https://sms.arkesel.com/api/v2/sms/send"

        payload ={
            "sender":sender,
            "message":message,
            "recipients": recipients,
            "scheduled_date" : scheduled_date
        }
        response = requests.post(SEND_SMS_URL, headers=header,json=payload)
        print (response.status_code)
    # scheduledSms('Trial','just trying this',['0248649732'],"2021-06-14 08:50 AM")


    
    def  webhookSms(sender:str, message:str, recipients:array.array, callback_url:str):
        header = {"api-key":API_KEY , 'Content-Type': 'application/json', 'Accept':'application/json'}
        SEND_SMS_URL = "https://sms.arkesel.com/api/v2/sms/send"

        payload ={
            "sender":sender,
            "message":message,
            "recipients": recipients,
            "callback_url" : callback_url
        }
        response = requests.post(SEND_SMS_URL, headers=header,json=payload)
        print (response.status_code)
    

    def voice_sms(voice_file:str, recipients:array.array):
       URL = "https://sms.arkesel.com/api/v2/sms/voice/send"
       header = {"api-key":API_KEY , 'Content-Type': 'application/json', 'Accept':'application/json'}
       payload={
           "voice_file":voice_file,
           "recipients":recipients
       }
       response = requests.post(URL, headers=header,json=payload)
       print(response.text)

   
    
    def send_group_sms(sender:str , group_name:str , message:str):
        URL = "https://sms.arkesel.com/api/v2/sms/send/contact-group"
        header = {"api-key":API_KEY , 'Content-Type': 'application/json', 'Accept':'application/json'}
        payload ={
            "sender":sender,
            "group_name":group_name,
            "message":message,
        }

        response = requests.post(URL, headers=header,json=payload)
        print (response.text)
    # send_group_sms("test","TEST GROUP","Here's a message")