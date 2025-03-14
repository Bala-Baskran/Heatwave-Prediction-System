import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# OpenWeather API
WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")

# Email Configuration
MAIL_SERVER = "smtp.gmail.com"
MAIL_PORT = 587
MAIL_USE_TLS = True
MAIL_USE_SSL = False
MAIL_USERNAME = os.getenv("MAIL_USERNAME")
MAIL_PASSWORD = os.getenv("MAIL_PASSWORD")

# Twilio API
TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_PHONE_NUMBER = os.getenv("TWILIO_PHONE_NUMBER")

# Flask Secret Key
SECRET_KEY = os.getenv("SECRET_KEY")
