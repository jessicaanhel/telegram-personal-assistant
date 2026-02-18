from app.usecases.trading.price_alert_handler import handle_price_alert_inline
from app.usecases.template_function.extended_function_handler import handle_extended_inline
from app.usecases.template_function.empty_function_handler import handle_empty_inline

async def inline_router(update, context):
    """
    Central router for all Telegram inline button callbacks.
    Delegates to the correct feature handler based on callback data.
    """
    query = update.callback_query
    data = query.data
    await query.answer()

    if data in ("setup_alert", "get_alerts_for_user"):
        return await handle_price_alert_inline(update, context)

    elif data == "run_extended_function":
        return await handle_extended_inline(update, context)

    # Template function button
    elif data in ("empty_function_1", "empty_function_2"):
        return await handle_empty_inline(update, context)

    await query.message.reply_text("Unknown action!")
    return None