import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler

from config import get_settings



logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")

def get_app() -> ApplicationBuilder:
    settings = get_settings()
    
    app = ApplicationBuilder().token().build(settings.)
    
    start_handler = CommandHandler('start', start)
    app.add_handler(start_handler)
    
    return app

if __name__ == '__main__':
    get_app().run_polling()