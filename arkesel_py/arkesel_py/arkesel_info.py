import os
import requests

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

class Info(object):
    def __init__(self) :
        pass
           
       
    def smsBalance():
        header = {"api-key":API_KEY ,  'Content-Type': 'application/json', 'Accept':'application/json'}
        BALANCE_URL =   "https://sms.arkesel.com/api/v2/clients/balance-details"
        response = session.get(BALANCE_URL,headers=header)
        print (response.text.encode('utf8'))
        # return response.json()
    # smsBalance()
    




    def smsDetails(DETAILS_URL):
        # DETAILS_URL = "https://sms.arkesel.com/api/v2/sms"/MESSAGE_ID
        header = {"api-key":API_KEY , 'Content-Type': 'application/json', 'Accept':'application/json'}
        response =  requests.get(DETAILS_URL , headers=header)
        print (response.text.encode('utf8'))
    # smsDetails("https://sms.arkesel.com/api/v2/sms"/Your MESSAGE_ID)

    