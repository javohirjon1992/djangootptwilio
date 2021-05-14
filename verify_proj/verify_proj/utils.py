import os
from twilio.rest import Client


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = os.environ['AC110135087bad03072e3049b68186ca6c']
auth_token = os.environ['b037eb435f906272b051ac4ff9b6c5d5']
client = Client(account_sid, auth_token)

def send_sms(user_code, phone_number):
    message = client.messages.create(
                     body=f"Salom sizning kodingiz {user_code}",
                     from_='+16085355989',
                     to=f'{phone_number}'
                 )

    print(message.sid)