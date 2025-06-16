from warnings import filterwarnings
from telegram import Update
from telegram.ext import ConversationHandler, CallbackQueryHandler, MessageHandler, filters
from telegram.warnings import PTBUserWarning

from functions.empty_function_1.bot import empty_function_1
from handlers.inline_handler import inline_button_handler
from utils.constants import EMPTY_FUNCTION_1, EMPTY_FUNCTION_2
filterwarnings(action="ignore", message=r".*CallbackQueryHandler", category=PTBUserWarning)

app = None

def init_app_empty_handler(app_instance):
    global app
    app = app_instance

async def ask_param1_empty_function(update: Update, context):
    if update.message.text.lower() == "/start":
        return await app.reset_and_start(update, context)

    try:
        context.user_data['param1'] = float(update.message.text)  # Convert the input to float
    except ValueError:
        await update.message.reply_text("Invalid input for param1. Please enter a valid number.")
        return EMPTY_FUNCTION_1

    await update.message.reply_text("Please enter the second parameter (param2) for Empty Function 1:")
    return EMPTY_FUNCTION_2

async def ask_param2_empty_function(update: Update, context):
    if update.message.text.lower() == "/start":
        return await reset_and_start(update, context)

    try:
        context.user_data['param2'] = float(update.message.text)  # Convert the input to float
    except ValueError:
        await update.message.reply_text("Invalid input for param2. Please enter a valid number.")
        return EMPTY_FUNCTION_2

    param1 = context.user_data['param1']
    param2 = context.user_data['param2']

    empty_function_1(param1, param2)

    await update.message.reply_text(f"Empty_Function_1 executed with param1={param1} and param2={param2}.")
    return ConversationHandler.END


conv_handler_empty_1 = ConversationHandler(
    entry_points=[CallbackQueryHandler(inline_button_handler, pattern="^empty_function_1$")],
    states={
        EMPTY_FUNCTION_1: [MessageHandler(filters.TEXT, ask_param1_empty_function)],
        EMPTY_FUNCTION_2: [MessageHandler(filters.TEXT, ask_param2_empty_function)],
    },
    fallbacks=[],
)
