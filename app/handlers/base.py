from settings import (
    get_settings,
    ProjectSettings,
)
from telegram import Update
from telegram.ext import ContextTypes


async def start_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    settings: ProjectSettings = get_settings()
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=settings.GREETING_TEXT,
    )
