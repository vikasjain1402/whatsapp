import os
def sendwhatsappmessage(message):
    '''
    message: message to be sent
    '''
    auth_token=os.environ['auth_token']
    account_sid=os.environ['account_sid']
    my_phone_no=os.environ['my_phone_no']
    from twilio.rest import Client
    client=Client(account_sid,auth_token)
    to=f"whatsapp:+91{my_phone_no}"
    from_="whatsapp:+14155238886"
    body=message
    message=client.messages.create(from_=from_,body=body,to=to)
    print(message.status)
if __name__=="__main__":
    sendwhatsappmessage("test message")