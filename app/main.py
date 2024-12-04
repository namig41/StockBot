import logging

from app.settings import (
    get_settings,
    ProjectSettings,
)
from handlers.base import start_handler
from handlers.products import get_all_products_handler
from telegram.ext import (
    Application,
    ApplicationBuilder,
    CommandHandler,
)


logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO,
)


def get_app() -> Application:
    settings: ProjectSettings = get_settings()

    app: Application = ApplicationBuilder().token(token=settings.TG_BOT_TOKEN).build()

    start_command_handler: CommandHandler = CommandHandler("start", start_handler)
    get_all_products_command_handler: CommandHandler = CommandHandler(
        "products", get_all_products_handler,
    )
    app.add_handler(start_command_handler)
    app.add_handler(get_all_products_command_handler)

    return app


if __name__ == "__main__":
    get_app().run_polling()
