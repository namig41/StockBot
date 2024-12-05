from dataclasses import dataclass

from exceptions.base import ApplicationException


@dataclass(frozen=True, eq=False)
class BatchListRequestException(ApplicationException):
    status_code: int
    response_content: str

    @property
    def message(self):
        return "Ошибка при получения продуктов"
