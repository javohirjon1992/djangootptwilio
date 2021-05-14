import os
from twilio.rest import Client


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = os.environ['Your sid']
auth_token = os.environ['Your AUTH']
client = Client(account_sid, auth_token)

def send_sms(user_code, phone_number):
    message = client.messages.create(
                     body=f"Salom sizning kodingiz {user_code}",
                     from_='Your Number',
                     to=f'{phone_number}'
                 )

    print(message.sid)