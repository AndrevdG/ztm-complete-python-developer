from dotenv import load_dotenv
from twilio.rest import Client
import os

# load api user / pw from .env
load_dotenv()
TWILLO_USER = os.getenv("TWILLO_USER")
TWILLO_PASSWORD = os.getenv("TWILLO_PASSWORD")
MY_NUMBER = os.getenv("MY_NUMBER")
TW_NUMBER = os.getenv("TW_NUMBER")

client = Client(TWILLO_USER, TWILLO_PASSWORD)

client.api.account.messages.create(
    to=MY_NUMBER, from_=TW_NUMBER, body="Anybody home?"
)
