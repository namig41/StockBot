from dataclasses import dataclass

from exceptions.base import ApplicationException


@dataclass(frozen=True, eq=False)
class SchemasException(ApplicationException):
    @property
    def message(self):
        return "Ошибка при обработки аргументов"
