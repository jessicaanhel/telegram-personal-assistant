import os
from dotenv import load_dotenv

load_dotenv()

ASK_PARAM1_EXTENDED = 1
ASK_PARAM2_EXTENDED = 2
ASK_PARAM3_EXTENDED = 3
ASK_PARAM4_EXTENDED = 4

EMPTY_FUNCTION_1 = 5
EMPTY_FUNCTION_2 = 6

TELEGRAM_BOT_TOKEN = os.environ.get("TELEGRAM_ANGEL_TOKEN")
ANGELA_TELEGRAM_USERID = int(os.environ.get("ANGELA_TELEGRAM_USERID"))
MONGO_URI = "mongodb://localhost:27017/"
DB_NAME = "coin_angel"

