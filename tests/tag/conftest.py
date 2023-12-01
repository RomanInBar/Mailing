from datetime import datetime

import pytest

from client.models import ClientORM
from client.schemas import ClientCreate
from mailing.models import MailingORM
from mailing.schemas import MailingCreate
from utils.services import create_object
from utils.unitofwork import ABCUnitOfWork, UnitOfWork


@pytest.fixture(scope="module")
async def client():
    uow: ABCUnitOfWork = UnitOfWork(ClientORM)
    client = await create_object(uow, ClientCreate(email="test1@mail.ru"))
    return (uow, client)


@pytest.fixture(scope="module")
async def mailing():
    uow: ABCUnitOfWork = UnitOfWork(MailingORM)
    mailing = await create_object(
        uow, MailingCreate(start=datetime.utcnow(), message="test mailing №:1")
    )
    return (uow, mailing)
