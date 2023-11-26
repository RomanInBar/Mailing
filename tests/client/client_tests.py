import pytest
import sys
sys.path.append('c:\\Users\\Roman\\Desktop\\Project\\Mailing')

from utils.services import (
    get_object,
    get_all_objects,
    create_object,
    update_object,
    get_total_objects,
    delete_object)
from client.schemas import ClientUpdate
from client.models import ClientORM


class TestsOfClients:
    async def test_create_clients(self, uow, clients_data):
        for client in clients_data:
            client: ClientORM = await create_object(uow, client)
        total: int = await get_total_objects(uow)
        assert total == 5

    async def test_update_client(self, uow):
        await update_object(uow, 1, ClientUpdate(email='update@mail.ru'))
        client: ClientORM = await get_object(uow, id=1)
        assert client.email == 'update@mail.ru' 
        
    async def test_get_client(self, uow):
        client: ClientORM = await get_object(uow, id=2)
        assert client.email == 'test2@mail.ru'

    async def test_get_all_client(self, uow):
        client: list = await get_all_objects(uow)
        total: int = len(client)
        assert total == 5

    async def test_delete_client(self, uow):
        await delete_object(uow, 1)
        total: int = await get_total_objects(uow)
        assert total == 4
        client: ClientORM = await get_object(uow, id=1)
        assert client is None
   