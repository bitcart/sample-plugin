from dishka import Provider, provide_all

from api.plugins import DIScope
from modules.bitcart.testapi.services.crud.reviews import ReviewRepository


class RepositoriesProvider(Provider):
    request_provides = provide_all(
        ReviewRepository,
        scope=DIScope.SESSION,
    )
