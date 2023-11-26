import pytest
from datetime import datetime

from utils.unitofwork import ABCUnitOfWork, UnitOfWork
from utils.services import create_object
from client.schemas import ClientCreate
from mailing.schemas import MailingCreate
from client.models import ClientORM
from mailing.models import MailingORM


@pytest.fixture(scope='module')
async def client():
    uow: ABCUnitOfWork = UnitOfWork(ClientORM)
    client = await create_object(uow, ClientCreate(email='test1@mail.ru'))
    return (uow, client)


@pytest.fixture(scope='module')
async def mailing():
    uow: ABCUnitOfWork = UnitOfWork(MailingORM)
    mailing = await create_object(uow, MailingCreate(start=datetime.utcnow(), message='test mailing №:1'))
    return (uow, mailing)
