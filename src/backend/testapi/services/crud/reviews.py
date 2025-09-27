from api.services.crud import CRUDRepository, CRUDService
from modules.bitcart.testapi import models


class ReviewRepository(CRUDRepository[models.Review]):
    model_type = models.Review


class ReviewService(CRUDService[models.Review]):
    repository_type = ReviewRepository
