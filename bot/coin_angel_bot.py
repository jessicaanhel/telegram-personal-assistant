from telegram.ext import Application
from bot.config import TELEGRAM_TOKEN

class CoinAngelBot:
    def __init__(self, token=TELEGRAM_TOKEN):
        self.application = Application.builder().token(token).build()

    def add_handler(self, handler):
        self.application.add_handler(handler)

    def add_error_handler(self, handler):
        self.application.add_error_handler(handler)

    def run(self):
        print("Starting CoinAngel Bot...")
        self.application.run_polling()

    async def send_message(self, user_id, text):
        await self.application.bot.send_message(chat_id=user_id, text=text)
