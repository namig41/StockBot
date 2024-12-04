from handlers.converters.products import convert_products_dtos_to_message
from telegram import Update
from telegram.ext import ContextTypes

from containers.factories import get_container
from dtos.product import ProductListItemDTO
from exceptions.base import ApplicationException
from services.web import BaseChatWebService


async def get_all_products_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    container = get_container()
    async with container() as request_container:
        try:
            service: BaseChatWebService = await request_container.get(
                BaseChatWebService,
            )
            products: list[ProductListItemDTO] = await service.get_all_products()
            await context.bot.send_message(
                chat_id=update.effective_chat.id,
                text=convert_products_dtos_to_message(products),
            )
        except ApplicationException as exception:
            await context.bot.send_message(
                chat_id=update.effective_chat.id,
                text=exception.message,
            )
