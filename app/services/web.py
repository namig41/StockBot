from abc import (
    ABC,
    abstractmethod,
)
from dataclasses import dataclass
from urllib.parse import urljoin

from httpx import AsyncClient

from dtos.batch import BatchListItemDTO
from exceptions.batches import BatchListRequestException
from services.constants import BATCH_LIST_URI
from services.converters.products import convert_batch_response_to_chat_dto


@dataclass
class BaseChatWebService(ABC):
    http_client: AsyncClient
    base_url: str

    @abstractmethod
    async def get_all_batches(self) -> list[BatchListItemDTO]: ...


@dataclass
class StockWebService(BaseChatWebService):

    async def get_all_batches(self) -> list[BatchListItemDTO]:
        response = await self.http_client.get(
            url=urljoin(base=self.base_url, url=BATCH_LIST_URI),
        )

        if not response.is_success:
            raise BatchListRequestException(
                status_code=response.status_code,
                response_content=response.content.decode(),
            )

        json_data = response.json()

        return [
            convert_batch_response_to_chat_dto(batch_data=batch_data)
            for batch_data in json_data["batches"]
        ]
