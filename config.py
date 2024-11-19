from dotenv import load_dotenv
import os

load_dotenv('dev_vars.env')

ACCESS_KEY = os.getenv('ACCESS_KEY')
OPENAI_TOKEN = os.getenv('OPENAI_TOKEN')

KEYWORDS = [
        'Listen_Joi',
        'Ok_Joi'
    ]

MICROPHONE_INDEX = -1

# spotify keys
REDIRECT_URI = os.getenv('REDIRECT_URI')
MY_SPOTIFY_USERNAME = os.getenv('MY_SPOTIFY_USERNAME')
SPOTIFY_DEVICE_ID = os.getenv('SPOTIFY_DEVICE_ID')
SPOTIFY_CLIENT_ID = os.getenv('SPOTIFY_CLIENT_ID')
SPOTIFY_CLIENT_SECRET = os.getenv('SPOTIFY_CLIENT_SECRET')

# for self-made spotify control
BASE_64 = os.getenv('BASE_64')
REFRESH_TOKEN = os.getenv('REFRESH_TOKEN')

GMAIL_API_KEY = os.getenv('GMAIL_API_KEY')
