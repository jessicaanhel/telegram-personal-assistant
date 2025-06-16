import logging
from telegram.ext import ContextTypes
from handlers.price_alert_handler import conv_handler_setup_alerts, init_app_price_alert_handler
from handlers.extended_function_handler import conv_handler_extended, init_app_extended_handler
from handlers.empty_function_handler import conv_handler_empty_1, init_app_empty_handler
from handlers.inline_handler import inline_button_handler
from telegram.ext import CommandHandler, CallbackQueryHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import ConversationHandler

from coin_angel_bot import CoinAngelBot

class App:
    def __init__(self):
        self.bot = CoinAngelBot()

    async def start_command(self, update, context):
        user = update.effective_user

        buttons = [
            [InlineKeyboardButton("Create Price Alert", callback_data="setup_alert"),
             InlineKeyboardButton("My Alerts", callback_data="get_alerts_for_user")],
            [InlineKeyboardButton("Empty Function 2", callback_data="empty_function_2"),
             InlineKeyboardButton("Run my extended function", callback_data="run_extended_function")]
        ]
        markup = InlineKeyboardMarkup(buttons)

        await update.message.reply_text(
            f"Hello, {user.first_name}! Welcome to your coin angel. Make your choice: Your user ID is: {user.id}",
            reply_markup=markup
        )
        return ConversationHandler.END

    async def error_handler(self, update: object, context: ContextTypes.DEFAULT_TYPE) -> None:
        logging.error("Exception occurred", exc_info=context.error)


    def register_handlers(self):
        self.bot.add_handler(CommandHandler("start", self.start_command))
        self.bot.add_handler(conv_handler_extended)
        self.bot.add_handler(conv_handler_empty_1)
        self.bot.add_handler(conv_handler_setup_alerts)
        self.bot.add_error_handler(self.error_handler)
        self.bot.add_handler(CallbackQueryHandler(inline_button_handler))

    def run(self):
        self.register_handlers()
        self.bot.run()

if __name__ == "__main__":
    app = App()
    init_app_empty_handler(app)
    init_app_extended_handler(app)
    init_app_price_alert_handler(app)
    app.run()