from abc import (
    ABC,
    abstractmethod,
)
from typing import (
    Generic,
    TypeVar,
)


BS = TypeVar("BS")


class BaseBatchesSchemas(ABC, Generic[BS]):

    @staticmethod
    @abstractmethod
    def parse(message: str) -> BS: ...
