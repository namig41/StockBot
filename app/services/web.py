from abc import (
    ABC,
    abstractmethod,
)
from dataclasses import dataclass
from urllib.parse import urljoin

from httpx import AsyncClient

from dtos.batch import BatchListItemDTO
from services.constants import BATCH_LIST_URI
from services.converters.batches import (
    convert_batch_data_to_batch_dto,
    convert_batch_dto_to_batch_data,
)
from services.exceptions.batches import BatchListRequestException


@dataclass
class BaseChatWebService(ABC):
    http_client: AsyncClient
    base_url: str

    @abstractmethod
    async def get_all_batches(self) -> list[BatchListItemDTO]: ...

    @abstractmethod
    async def get_batch(self, reference: str) -> BatchListItemDTO: ...

    @abstractmethod
    async def add_batch(self, batch: BatchListItemDTO) -> BatchListItemDTO: ...


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
            convert_batch_data_to_batch_dto(batch_data=batch_data)
            for batch_data in json_data["batches"]
        ]

    async def get_batch(self, reference: str) -> BatchListItemDTO:
        response = await self.http_client.get(
            url=urljoin(base=self.base_url, url=f"{BATCH_LIST_URI}{reference}"),
        )

        if not response.is_success:
            raise BatchListRequestException(
                status_code=response.status_code,
                response_content=response.content.decode(),
            )

        batch_data = response.json()

        return convert_batch_data_to_batch_dto(batch_data=batch_data)

    async def add_batch(self, batch: BatchListItemDTO) -> BatchListItemDTO:

        batch_data: dict = convert_batch_dto_to_batch_data(batch)

        response = await self.http_client.post(
            url=urljoin(base=self.base_url, url=f"{BATCH_LIST_URI}"),
            json=batch_data,
        )

        if not response.is_success:
            raise BatchListRequestException(
                status_code=response.status_code,
                response_content=response.content.decode(),
            )

        batch_data = response.json()

        return convert_batch_data_to_batch_dto(batch_data=batch_data)
