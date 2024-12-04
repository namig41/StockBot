from abc import (
    ABC,
    abstractmethod,
)
from dataclasses import dataclass
from urllib.parse import urljoin

from httpx import AsyncClient

from dtos.product import ProductListItemDTO
from exceptions.products import ProductListRequestException
from services.constants import PRODUCT_LIST_URI
from services.converters.products import convert_product_response_to_chat_dto


@dataclass
class BaseChatWebService(ABC):
    http_client: AsyncClient
    base_url: str

    @abstractmethod
    async def get_all_products(self) -> list[ProductListItemDTO]: ...


@dataclass
class StockWebService(BaseChatWebService):

    async def get_all_products(self) -> list[ProductListItemDTO]:
        response = await self.http_client.get(
            url=urljoin(base=self.base_url, url=PRODUCT_LIST_URI),
        )

        if not response.is_success:
            raise ProductListRequestException(
                status_code=response.status_code,
                response_content=response.content.decode(),
            )

        json_data = response.json()

        return [
            convert_product_response_to_chat_dto(product_data=product_data)
            for product_data in json_data["batches"]
        ]
