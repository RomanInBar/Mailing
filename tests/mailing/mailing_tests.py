import pytest

from utils.services import (
    get_object,
    get_all_objects,
    create_object,
    update_object,
    get_total_objects,
    delete_object)
from mailing.schemas import MailingUpdate
from mailing.models import MailingORM


class TestsOfMailings:
    async def test_create_mailings(self, uow, mailings_data):
        for mailing in mailings_data:
            mailing: MailingORM = await create_object(uow, mailing)
        total: int = await get_total_objects(uow)
        assert total == 5

    async def test_update_mailing(self, uow):
        await update_object(uow, 1, MailingUpdate(message='updated mailing'))
        mailing: MailingORM = await get_object(uow, id=1)
        assert mailing.message == 'updated mailing' 
        
    async def test_get_mailing(self, uow):
        mailing: MailingORM = await get_object(uow, id=2)
        assert mailing.message == 'test mailing №:2'

    async def test_get_all_mailings(self, uow):
        mailing: list = await get_all_objects(uow)
        total: int = len(mailing)
        assert total == 5

    async def test_delete_mailing(self, uow):
        await delete_object(uow, 1)
        total: int = await get_total_objects(uow)
        assert total == 4
        mailing: MailingORM = await get_object(uow, id=1)
        assert mailing is None

    