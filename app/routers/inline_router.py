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

    # non-conversational functions only
    if data == "get_alerts_for_user":
        from app.usecases.trading.price_alert_handler import show_user_alerts
        return await show_user_alerts(update, context)

    elif data == "return_home":
        from app.usecases.trading.price_alert_handler import return_home
        return await return_home(update, context)

    elif data == "reset_and_start":
        return await context.bot_data["app"].reset_and_start(update, context)

    return None