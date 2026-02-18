from utils.constants import ASK_PARAM1_EXTENDED, EMPTY_FUNCTION_1, EMPTY_FUNCTION_2


async def inline_button_handler(update, context):
    query = update.callback_query
    data = query.data
    await query.answer()

    if data == "run_extended_function":
        await query.message.reply_text("Please enter the first parameter (param1):")
        return ASK_PARAM1_EXTENDED

    elif data == "empty_function_1":
        await query.message.reply_text("Please enter the first parameter (param1) for Empty Function 1:")
        return EMPTY_FUNCTION_1

    elif data == "empty_function_2":
        await query.message.reply_text("Empty function 2 triggered. Implement later.")
        return EMPTY_FUNCTION_2

    return None