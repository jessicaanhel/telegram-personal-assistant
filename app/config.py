import os

from app.utils.settings_utils import get_env

ENV = os.getenv("ENV", "local")

if ENV == "local":
    from dotenv import load_dotenv
    load_dotenv()

# Tokens
TELEGRAM_TOKEN = get_env("TELEGRAM_ANGEL_TOKEN")
TELEGRAM_CHAT_ID = ("X", "NO-CHAT-ID")
TELEGRAM_USER_ID = get_env("ANGELA_TELEGRAM_USERID", "NO-USER-ID")

GITHUB_TOKEN = get_env("GITHUB_TOKEN")

#External services
BANDSINTOWN_APP_ID = "X"

# App config
MONGO_URI = "mongodb://localhost:27017/"
DB_NAME = "coin_angel"

# Bot states
ASK_PARAM1_EXTENDED = 1
ASK_PARAM2_EXTENDED = 2
ASK_PARAM3_EXTENDED = 3
ASK_PARAM4_EXTENDED = 4

EMPTY_FUNCTION_1 = 5
EMPTY_FUNCTION_2 = 6

CHECK_INTERVAL_MINUTES = 60
