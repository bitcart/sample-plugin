# ruff: noqa: T201
from typing import Any

from fastapi import FastAPI

from api import models
from api.plugins import BasePlugin, update_metadata
from modules.bitcart.testapi.schemas import TestEventMessage
from modules.bitcart.testapi.views import router


class Plugin(BasePlugin):
    name = "testapi"

    def setup_app(self, app: FastAPI) -> None:
        app.include_router(router, prefix="/reviews", tags=["reviews"])

    async def startup(self) -> None:
        self.context.register_hook("db_create_invoice", self.handle_invoice)
        self.register_template("test", applicable_to="product")
        self.context.register_event("test_event", ["message"])
        self.context.register_event_handler("test_event", self.handle_event)
        self.context.register_event_handler("invoice_status", self.handle_event)
        self.context.register_hook("pre_deploy", self.pre_deploy)
        self.context.register_hook("post_deploy", self.post_deploy)

        # start the needed app-level services
        from modules.bitcart.testapi.ioc import TO_PRELOAD

        for service in TO_PRELOAD:
            await self.container.get(service)

    async def shutdown(self) -> None:
        pass

    async def worker_setup(self) -> None:
        pass

    async def handle_invoice(self, invoice: models.Invoice) -> None:
        print("Invoice created", invoice)
        await self.context.publish_event("test_event", TestEventMessage(message="Hello world!"))
        update_metadata(invoice, "rating", 0)

    async def handle_event(self, event: str, event_data: dict[str, Any]) -> None:
        print("Event received", event, event_data)

    async def pre_deploy(self, task_id: str, task: dict[str, Any]) -> None:
        print("Pre deploy", task_id, task)

    async def post_deploy(self, task_id: str, task: dict[str, Any], success: bool, output: str) -> None:
        print("Post deploy", task_id, task, success, output)
