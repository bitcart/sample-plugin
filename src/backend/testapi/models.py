from sqlalchemy import ForeignKey, Text
from sqlalchemy.orm import Mapped, mapped_column

from api.models import RecordModel


class PluginBaseModel(RecordModel):
    TABLE_PREFIX = "testapi"

    __abstract__ = True


class Review(PluginBaseModel):
    __tablename__ = "reviews"

    name: Mapped[str] = mapped_column(Text)
    user_id: Mapped[str | None] = mapped_column(Text, ForeignKey("users.id", ondelete="SET NULL"))
