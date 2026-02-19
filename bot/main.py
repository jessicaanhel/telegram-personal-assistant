import logging
from telegram.ext import CommandHandler, CallbackQueryHandler, ConversationHandler, ContextTypes
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

from coin_angel_bot import CoinAngelBot
from bot.routers.inline_router import inline_router

from bot.commands.trading.price_alert_handler import conv_handler_setup_alerts
from bot.commands.template_function.extended_function_handler import get_extended_conv_handler, handle_extended_inline
from bot.commands.template_function.empty_function_handler import get_empty_1_conv_handler, handle_empty_inline


class AppManager:
    def __init__(self):
        self.bot = CoinAngelBot()
        self.conv_handler_extended = get_extended_conv_handler(handle_extended_inline)
        self.conv_handler_empty_1 = get_empty_1_conv_handler(handle_empty_inline)
        self.register_handlers()


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

    async def reset_and_start(self, update, context):
        logging.info("Reset command executed")
        context.user_data.clear()
        context.chat_data.clear()
        return await self.start_command(update, context)

    @staticmethod
    async def error_handler(update: object, context: ContextTypes.DEFAULT_TYPE) -> None:
        logging.error("Exception occurred", exc_info=context.error)

    def register_handlers(self):
        """Register all feature conversation routers"""
        #Conversation
        self.bot.add_handler(conv_handler_setup_alerts)
        self.bot.add_handler(self.conv_handler_extended)
        self.bot.add_handler(self.conv_handler_empty_1)

        #non-conversation
        self.bot.add_handler(CommandHandler("start", self.start_command))

        #Register router manager for inline button
        self.bot.add_handler(CallbackQueryHandler(inline_router))
        self.bot.add_error_handler(self.error_handler)

    def run(self):
        self.bot.application.bot_data["app"] = self
        self.bot.run()


if __name__ == "__main__":
    app = AppManager()
    app.run()