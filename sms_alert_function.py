from flask.cli import load_dotenv
from twilio.rest import Client
import os
from dotenv import load_dotenv


load_dotenv()
def sms():
    account_sid = os.getenv("TWILIO_ACCOUNT_SID")
    auth_token = os.getenv("TWILIO_AUTH_TOKEN")
    twilio_number = +16206757645
    target_number = +919030232240
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body = "This is a message from SenitelAI squad, Something mischievous is happening🤔 at the location you specified to us.",
        from_ = twilio_number,
        to = target_number
    )

    print(message.body)