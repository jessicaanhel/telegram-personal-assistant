from warnings import filterwarnings
from telegram import Update
from telegram.ext import CallbackQueryHandler, ConversationHandler, MessageHandler, filters
from telegram.warnings import PTBUserWarning

from functions.calculation_script.calculation_script import my_function_extended
from handlers.inline_handler import inline_button_handler
from utils.constants import (
    ASK_PARAM1_EXTENDED,
    ASK_PARAM2_EXTENDED,
    ASK_PARAM3_EXTENDED,
    ASK_PARAM4_EXTENDED,
)

filterwarnings(action="ignore", message=r".*CallbackQueryHandler", category=PTBUserWarning)

app = None

def init_app_extended_handler(app_instance):
    global app
    app = app_instance

async def ask_param1_extended(update: Update, context):
    if update.message.text.lower() == "/start":
        return await app.reset_and_start(update, context)

    try:
        context.user_data['param1'] = float(update.message.text)  # Convert the input to float
    except ValueError:
        await update.message.reply_text("Invalid input for param1. Please enter a valid number.")
        return ASK_PARAM1_EXTENDED

    await update.message.reply_text("Please enter the second parameter (param2):")
    return ASK_PARAM2_EXTENDED


async def ask_param2_extended(update: Update, context):
    if update.message.text.lower() == "/start":
        return await app.reset_and_start(update, context)

    try:
        context.user_data['param2'] = float(update.message.text)  # Convert the input to float
    except ValueError:
        await update.message.reply_text("Invalid input for param2. Please enter a valid number.")
        return ASK_PARAM2_EXTENDED

    await update.message.reply_text("Please enter the third parameter (param3):")
    return ASK_PARAM3_EXTENDED


async def ask_param3_extended(update: Update, context):
    if update.message.text.lower() == "/start":
        return await app.reset_and_start(update, context)

    try:
        context.user_data['param3'] = float(update.message.text)  # Convert the input to float
    except ValueError:
        await update.message.reply_text("Invalid input for param3. Please enter a valid number.")
        return ASK_PARAM3_EXTENDED

    await update.message.reply_text("Please enter the fourth parameter (param4):")
    return ASK_PARAM4_EXTENDED


async def ask_param4_extended(update: Update, context):
    if update.message.text.lower() == "/start":
        return await app.reset_and_start(update, context)

    try:
        context.user_data['param4'] = float(update.message.text)  # Convert the input to float
    except ValueError:
        await update.message.reply_text("Invalid input for param4. Please enter a valid number.")
        return ASK_PARAM4_EXTENDED

    param1 = context.user_data['param1']
    param2 = context.user_data['param2']
    param3 = context.user_data['param3']
    param4 = context.user_data['param4']

    result = my_function_extended(param1, param2, param3, param4)

    await update.message.reply_text(f"Extended function executed with result: {result}")
    return ConversationHandler.END


conv_handler_extended = ConversationHandler(
    entry_points=[CallbackQueryHandler(inline_button_handler, pattern="^run_extended_function$")],
    states={
        ASK_PARAM1_EXTENDED: [MessageHandler(filters.TEXT, ask_param1_extended)],
        ASK_PARAM2_EXTENDED: [MessageHandler(filters.TEXT, ask_param2_extended)],
        ASK_PARAM3_EXTENDED: [MessageHandler(filters.TEXT, ask_param3_extended)],
        ASK_PARAM4_EXTENDED: [MessageHandler(filters.TEXT, ask_param4_extended)],
    },
    fallbacks=[],
)
