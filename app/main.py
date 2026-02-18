import logging
from telegram.ext import CommandHandler, CallbackQueryHandler, ConversationHandler, ContextTypes
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

from coin_angel_bot import CoinAngelBot
from app.routers.inline_router import inline_router

from app.usecases.trading.price_alert_handler import init_app_price_alert_handler, conv_handler_setup_alerts
from app.usecases.template_function.extended_function_handler import init_app_extended_handler, get_extended_conv_handler
from app.usecases.template_function.empty_function_handler import init_app_empty_handler, get_empty_1_conv_handler

conv_handler_extended = get_extended_conv_handler(inline_router)
conv_handler_empty_1 = get_empty_1_conv_handler(inline_router)

class App:
    def __init__(self):
        self.bot = CoinAngelBot()
        self.register_global_handlers()

    def register_global_handlers(self):
        """Register global routers like start, inline callbacks, error handler"""
        self.bot.add_handler(CommandHandler("start", self.start_command))
        self.bot.add_handler(CallbackQueryHandler(inline_router))
        self.bot.add_error_handler(self.error_handler)

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
            f"Hello, {user.first_name}! Welcome to your coin angel. Your user ID: {user.id}",
            reply_markup=markup
        )
        return ConversationHandler.END

    async def error_handler(self, update: object, context: ContextTypes.DEFAULT_TYPE) -> None:
        logging.error("Exception occurred", exc_info=context.error)

    def register_routers(self):
        """Register all feature conversation routers"""
        self.bot.add_handler(conv_handler_extended)
        self.bot.add_handler(conv_handler_empty_1)
        self.bot.add_handler(conv_handler_setup_alerts)

    def run(self):
        self.register_routers()
        self.bot.run()


if __name__ == "__main__":
    app = App()
    # Initialize features (inject app if needed)
    init_app_empty_handler(app)
    init_app_extended_handler(app)
    init_app_price_alert_handler(app)
    app.run()