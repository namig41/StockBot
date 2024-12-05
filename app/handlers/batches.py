from handlers.converters.batches import (
    convert_batch_dtos_to_message,
    convert_batches_dtos_to_message,
)
from schemas.batches import (
    AddBatchSchemas,
    GetBatchSchemas,
)
from telegram import Update
from telegram.ext import ContextTypes

from containers.factories import get_container
from dtos.batch import BatchListItemDTO
from exceptions.base import ApplicationException
from services.web import BaseChatWebService


async def get_all_batches_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    container = get_container()
    async with container() as request_container:
        try:
            service: BaseChatWebService = await request_container.get(
                BaseChatWebService,
            )
            batches: list[BatchListItemDTO] = await service.get_all_batches()
            await context.bot.send_message(
                chat_id=update.effective_chat.id,
                text=convert_batches_dtos_to_message(batches),
                parse_mode="MarkdownV2",
            )
        except ApplicationException as exception:
            await context.bot.send_message(
                chat_id=update.effective_chat.id,
                text=exception.message,
            )


async def get_batch_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    container = get_container()
    async with container() as request_container:
        try:
            service: BaseChatWebService = await request_container.get(
                BaseChatWebService,
            )
            reference: str = GetBatchSchemas.parse(update.message.text)

            batch: BatchListItemDTO = await service.get_batch(reference=reference)
            await context.bot.send_message(
                chat_id=update.effective_chat.id,
                text=convert_batch_dtos_to_message(batch),
            )
        except ApplicationException as exception:
            await context.bot.send_message(
                chat_id=update.effective_chat.id,
                text=exception.message,
            )


async def add_batch_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    container = get_container()
    async with container() as request_container:
        try:
            service: BaseChatWebService = await request_container.get(
                BaseChatWebService,
            )
            reference, sku = AddBatchSchemas.parse(update.message.text)

            batch: BatchListItemDTO = await service.add_batch(
                BatchListItemDTO(reference=reference, sku=sku),
            )

            await context.bot.send_message(
                chat_id=update.effective_chat.id,
                text=("Продукт добавлен\n" f"{convert_batch_dtos_to_message(batch)}"),
            )
        except ApplicationException as exception:
            await context.bot.send_message(
                chat_id=update.effective_chat.id,
                text=exception.message,
            )
