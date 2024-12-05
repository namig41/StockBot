from dishka import (
    provide,
    Provider,
    Scope,
)
from httpx import AsyncClient
from settings import ProjectSettings

from services.web import (
    BaseChatWebService,
    StockWebService,
)


class DefaultProvider(Provider):
    @provide(scope=Scope.APP)
    def get_settings(self) -> ProjectSettings:
        return ProjectSettings()

    @provide(scope=Scope.REQUEST)
    def get_http_client(self) -> AsyncClient:
        return AsyncClient()

    @provide(scope=Scope.APP)
    def get_product_web_service(self) -> BaseChatWebService:
        return StockWebService(
            http_client=self.get_http_client(),
            base_url=self.get_settings().WEB_API_BASE_URL,
        )
