import pytest
from datetime import datetime

from mailing.schemas import MailingCreate
from utils.unitofwork import ABCUnitOfWork, UnitOfWork
from mailing.models import MailingORM


@pytest.fixture
def mailings_data():
    mailings = [
        MailingCreate(start=datetime.utcnow(), message='test mailing №:1'),
        MailingCreate(start=datetime.utcnow(), message='test mailing №:2'),
        MailingCreate(start=datetime.utcnow(), message='test mailing №:3'),
        MailingCreate(start=datetime.utcnow(), message='test mailing №:4'),
        MailingCreate(start=datetime.utcnow(), message='test mailing №:5'),
    ]
    return mailings


@pytest.fixture(scope='module')
def uow():
    uow: ABCUnitOfWork = UnitOfWork(MailingORM)
    return uow
