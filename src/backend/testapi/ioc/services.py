from typing import Any

from dishka import Provider, provide_all

from api.plugins import DIScope
from modules.bitcart.testapi.services.crud.reviews import ReviewService


class ServicesProvider(Provider):
    # here you can put all the request-level services (usually crud-ones)
    request_provides = provide_all(
        ReviewService,
        scope=DIScope.SESSION,
    )
    # here you put app-level services, usually those needing to start some background tasks or managing global state
    app_provides = provide_all(
        scope=DIScope.APP,
    )

    # by default the DI system is lazy, so no dependencies are loaded.
    # you have to manually call container.get in setup of your plugin, and inside the service you can execute extra
    # worker-only setup actions by checking settings.IS_WORKER
    # note that you need to utilize TO_PRELOAD manually, see code in plugin.py
    TO_PRELOAD: list[Any] = []

    # if you want to execute some kind of async background actions, create an async start method on your service, and then do
    # from dishka import decorate

    # @decorate
    # async def get_my_service(
    #     self,
    #     service: MyService,
    # ) -> AsyncIterator[MyService]:
    #     await service.start()
    #     yield service
