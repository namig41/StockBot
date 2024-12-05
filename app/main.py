import logging

from handlers.base import start_handler
from handlers.batches import get_all_batches_handler
from settings import (
    get_settings,
    ProjectSettings,
)
from telegram.ext import (
    Application,
    ApplicationBuilder,
    CommandHandler,
)


logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)


def get_app() -> Application:
    settings: ProjectSettings = get_settings()

    app: Application = ApplicationBuilder().token(token=settings.TG_BOT_TOKEN).build()

    start_command_handler: CommandHandler = CommandHandler("start", start_handler)
    get_all_batches_command_handler: CommandHandler = CommandHandler(
        "batches",
        get_all_batches_handler,
    )

    app.add_handler(start_command_handler)
    app.add_handler(get_all_batches_command_handler)

    return app


if __name__ == "__main__":
    get_app().run_polling()
