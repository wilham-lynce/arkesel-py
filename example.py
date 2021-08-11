from arkesel_py import ArkeselSMS
from arkesel_py import SmsInfo
from arkesel_py import ArkeselOtp


def sendBulkText():
    letter = ArkeselSMS()
    print (letter.sendSms("user" , "example file text" , ["0XXXXXXXXX"]))
# sendBulkText()

def checkBalance():
    checker= SmsInfo()
    print (checker.smsBalance())
# checkBalance()

def authenticate():
    send = ArkeselOtp()
    print (send.sendOtp(5, 6, "sms","This is OTP from tester, %otp_code%","0XXXXXXXXX","tester","numeric"))
# authenticate()

def VerifyCode():
    auth=ArkeselOtp()
    print (auth.verifyOtp("XXXXXX" ,"0XXXXXXXXX"))
# VerifyCode()
