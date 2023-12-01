import pytest

from client.schemas import ClientCreate


@pytest.fixture
def clients_data():
    clients = [
        ClientCreate(email="test1@mail.ru"),
        ClientCreate(email="test2@mail.ru"),
        ClientCreate(email="test3@mail.ru"),
        ClientCreate(email="test4@mail.ru"),
        ClientCreate(email="test5@mail.ru"),
    ]
    return clients
