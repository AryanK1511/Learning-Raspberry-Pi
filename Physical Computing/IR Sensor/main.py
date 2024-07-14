from gpiozero import MotionSensor
from twilio.rest import Client
from dotenv import load_dotenv
import os

load_dotenv()

account_sid = os.environ["TWILIO_ACCOUNT_SID"]
auth_token = os.environ["TWILIO_AUTH_TOKEN"]
client = Client(account_sid, auth_token)

def send_message():
    message = client.messages.create(
        body="Detected Movement",
        from_=os.environ["TWILIO_PHONE_NUMBER"],
        to=os.environ["TWILIO_PERSONAL_PHONE_NUMBER"],
    )

    print(message.body)

pir = MotionSensor(4)

while True:
    pir.wait_for_motion()
    print("You moved")
    send_message()
    pir.wait_for_no_motion()
    print("You stopped")
