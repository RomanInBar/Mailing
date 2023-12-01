import json

from client.models import ClientORM
from client.schemas import ClientUpdate
from utils.services import (create_object, delete_object, get_all_objects,
                            get_object, get_total_objects, update_object)


class TestsOfClientServices:
    async def test_create_clients(self, cuow, clients_data):
        for client in clients_data:
            client: ClientORM = await create_object(cuow, client)
        total: int = await get_total_objects(cuow)
        assert total == 5

    async def test_update_client(self, cuow):
        await update_object(cuow, 1, ClientUpdate(email="update@mail.ru"))
        client: ClientORM = await get_object(cuow, id=1)
        assert client.email == "update@mail.ru"

    async def test_get_client(self, cuow):
        client: ClientORM = await get_object(cuow, id=2)
        assert client.email == "test2@mail.ru"

    async def test_get_all_client(self, cuow):
        client: list = await get_all_objects(cuow)
        total: int = len(client)
        assert total == 5

    async def test_delete_client(self, cuow):
        await delete_object(cuow, 1)
        total: int = await get_total_objects(cuow)
        assert total == 4
        client: ClientORM = await get_object(cuow, id=1)
        assert client is None
