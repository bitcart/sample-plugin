from typing import Any

from fastapi import APIRouter

from api.plugins import DIRoute, register_scope
from api.utils.routing import create_crud_router
from modules.bitcart.testapi.schemas import CreateReview, DisplayReview, UpdateReview
from modules.bitcart.testapi.services.crud.reviews import ReviewService

router = APIRouter(route_class=DIRoute)

register_scope("reviews_management", "Create, list or edit reviews")


@router.get("/testpage")
async def testpage() -> Any:
    return {"testpage": "testpage"}


create_crud_router(
    CreateReview,
    UpdateReview,
    DisplayReview,
    ReviewService,
    required_scopes=["reviews_management"],
    router=router,
)
