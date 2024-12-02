from dataclasses import dataclass

from exceptions.base import ApplicationException

@dataclass(frozen=True, eq=False)
class ProductListRequestError(ApplicationException):
    status_code: int
    reponse_content: str
    
    @property
    def message(self):
        return "Ошибка при получения продуктов"