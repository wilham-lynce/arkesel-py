from arkesel_py.arkesel_py import arkesel_sms
from arkesel_py.arkesel_py import arkesel_otp

def sendBulkText():
    letter = arkesel_sms.ArkeselSMS()
    print (letter.sendSms("wilham" , "example file text" , ["0248649732"]))
# sendBulkText()

def checkBalance():
    checker  = arkesel_sms.SmsInfo()
    print (checker.smsBalance())
# checkBalance()

def authenticate():
    send = arkesel_otp.ArkeselOtp()
    print (send.sendOtp(5, 6, "sms","This is OTP from tester, %otp_code%","233XXXXXXXXX","tester","numeric"))
# authenticate()

def VerifyCode():
    auth =arkesel_otp.ArkeselOtp()
    print (auth.verifyOtp("XXXXXX" ,"233XXXXXXXXX"))
# VerifyCode()