from api.schemas.base import Schema, TimestampedSchema


class CreateReview(Schema):
    name: str


class UpdateReview(CreateReview):
    pass


class DisplayReview(CreateReview, TimestampedSchema):
    id: str
    user_id: str


class TestEventMessage(Schema):
    message: str
