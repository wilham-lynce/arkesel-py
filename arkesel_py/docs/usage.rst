=====
Usage
=====

To send SMS in a project using Arkesel::

    from arkesel_py.arkesel_py import ArkeselSMS
    from arkesel_py.arkesel_py import SmsInfo
    from arkesel_py.arkesel_py import ArkeselOTP
    from arkesel_py.arkesel_py import Contacts

#. class ArkeselSMS has the following methods::

       sendSms
       scheduledSms
       webhookSms
       sandBox
       voiceSms
       send_group_sms

#. class ArkeselOTP has the following methods::

       sendOtp
       verifyOtp
   
#. class SmsInfo has the following methods::

       smsBalance 
       smsDetails 


Sending Bulk SMS::


    
    def sendBulkText():
        letter = ArkeselSMS()
        print (letter.sendSms("user" , "example text" , ["0XXXXXXXXX"]))
    sendBulkText()

Sending Scheduled Bulk SMS::

    def sendBulkText():
        send = ArkeselSMS()
        print (send.scheduledSms('Trial','just trying this',['0XXXXXXXXX'],"2021-07-01 12:07 PM"))
    sendBulkText()

Sending Bulk SMS With Delivery Webhook

    def sendWithWebhook():
        send = ArkeselSMS()
        print (send.webhookSms('Trial','just trying this',['0XXXXXXXXX'],"https://aptinc.com/sms/delivery_webhook"))
