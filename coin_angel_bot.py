from telegram.ext import Application, CommandHandler, CallbackQueryHandler
from handlers.price_alert_handler import conv_handler_product_picker
from handlers.inline_handler import inline_button_handler
from handlers.extended_function_handler import conv_handler_extended
from handlers.empty_function_handler import conv_handler_empty_1
from handlers.start_handler import start_command
from utils.constants import TELEGRAM_BOT_TOKEN

class CoinAngelBot:
    def __init__(self, token=TELEGRAM_BOT_TOKEN):
        self.application = Application.builder().token(token).build()

    def register_handlers(self):
        self.application.add_handler(CommandHandler("start", start_command))
        self.application.add_handler(conv_handler_extended)
        self.application.add_handler(conv_handler_empty_1)
        self.application.add_handler(conv_handler_product_picker)
        self.application.add_handler(CallbackQueryHandler(inline_button_handler, pattern="^run_extended_function$"))
        self.application.add_handler(CallbackQueryHandler(inline_button_handler, pattern="^empty_function_1$"))
        self.application.add_handler(CallbackQueryHandler(inline_button_handler, pattern="^empty_function_2$"))
        self.application.add_handler(CallbackQueryHandler(inline_button_handler))  # Catch-all fallback

    def run(self):
        print("Starting CoinAngel Bot...")
        self.register_handlers()
        self.application.run_polling()

    async def send_message(self, user_id, text):
        await self.application.bot.send_message(chat_id=user_id, text=text)
