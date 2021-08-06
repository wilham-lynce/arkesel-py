# from arkesel_py.arkesel_py import arkesel_sms
# from arkesel_py.arkesel_py import arkesel_otp

from arkesel_py.arkesel_py import ArkeselSMS
from arkesel_py.arkesel_py import SmsInfo
from arkesel_py.arkesel_py import ArkeselOtp


def sendBulkText():
    letter = ArkeselSMS()
    print (letter.sendSms("wilham" , "example file text" , ["0248649732"]))
# sendBulkText()

def checkBalance():
    checker= SmsInfo()
    print (checker.smsBalance())
# checkBalance()

def authenticate():
    send = ArkeselOtp()
    print (send.sendOtp(5, 6, "sms","This is OTP from tester, %otp_code%","233XXXXXXXXX","tester","numeric"))
# authenticate()

def VerifyCode():
    auth=ArkeselOtp()
    print (auth.verifyOtp("XXXXXX" ,"233XXXXXXXXX"))
# VerifyCode()
