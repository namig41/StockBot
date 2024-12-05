from dataclasses import dataclass

from exceptions.base import ApplicationException


@dataclass(frozen=True, eq=False)
class ServicesException(ApplicationException):
    @property
    def message(self):
        return "Ошибка при обработке веб-запроса"
