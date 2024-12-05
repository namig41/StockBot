from dataclasses import dataclass

from services.exceptions.base import ServicesException


@dataclass(frozen=True, eq=False)
class BatchListRequestException(ServicesException):
    status_code: int
    response_content: str

    @property
    def message(self):
        return "Ошибка при получения продуктов"
