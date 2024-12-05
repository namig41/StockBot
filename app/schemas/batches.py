from schemas.base import BaseBatchesSchemas
from schemas.exceptions.base import SchemasException


class GetBatchesSchemas(BaseBatchesSchemas[None]):

    @staticmethod
    def parse(message: str) -> None: ...


class GetBatchSchemas(BaseBatchesSchemas[str]):

    @staticmethod
    def parse(message: str) -> str:
        args: list[str] = message.split()

        if len(args) != 2:
            raise SchemasException()

        return args[1]


class AddBatchSchemas(BaseBatchesSchemas[list[str]]):

    @staticmethod
    def parse(message: str) -> list[str]:
        args: list[str] = message.split()

        if len(args) != 3:
            raise SchemasException()

        return args[1:]
