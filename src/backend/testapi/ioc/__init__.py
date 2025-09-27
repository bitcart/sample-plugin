from dishka import Provider

from .repositories import RepositoriesProvider
from .services import ServicesProvider


def get_providers() -> list[Provider]:
    return [RepositoriesProvider(), ServicesProvider()]


TO_PRELOAD = ServicesProvider.TO_PRELOAD
