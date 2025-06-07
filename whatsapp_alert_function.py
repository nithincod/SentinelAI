from twilio.rest import Client
from dotenv import load_dotenv
import os
def whatsapp():
    account_sid = os.getenv("TWILIO_ACCOUNT_SID")
    auth_token = os.getenv("TWILIO_AUTH_TOKEN")
    client = Client(account_sid, auth_token)

    message = client.messages.create(
    body='This is a message from SenitelAI Squad, Something mischievous is happening🤔 at the location you specified to us.',
    from_='whatsapp:+14155238886',
    to='whatsapp:+919030232240'
    )

    print(message.sid)