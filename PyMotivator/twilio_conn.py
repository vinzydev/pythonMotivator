from twilio.rest import Client
from config import account_sid,auth_token,phone_num

'''
Set Twilio connection to whatsapp
'''
def set_twilio_connection(account_sid, auth_token):
    client = Client(account_sid, auth_token) 
    return client

def send_whatsapp_text(client,quote):
    message = client.messages.create( 
                              from_='whatsapp:+14155238886',  
                              body=quote,   
                              to=phone_num
                            )
    return message.sid

client = set_twilio_connection(account_sid,auth_token)