import pytest

from client.schemas import ClientCreate
from utils.unitofwork import ABCUnitOfWork, UnitOfWork
from client.models import ClientORM


@pytest.fixture
def clients_data():
    clients = [
        ClientCreate(email='test1@mail.ru'),
        ClientCreate(email='test2@mail.ru'),
        ClientCreate(email='test3@mail.ru'),
        ClientCreate(email='test4@mail.ru'),
        ClientCreate(email='test5@mail.ru')
    ]
    return clients


@pytest.fixture(scope='module')
def uow():
    uow: ABCUnitOfWork = UnitOfWork(ClientORM)
    return uow
