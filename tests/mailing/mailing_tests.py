import pytest

from mailing.models import MailingORM
from mailing.schemas import MailingUpdate
from utils.services import (create_object, delete_object, get_all_objects,
                            get_object, get_total_objects, update_object)


class TestsOfMailings:
    async def test_create_mailings(self, muow, mailings_data):
        for mailing in mailings_data:
            mailing: MailingORM = await create_object(muow, mailing)
        total: int = await get_total_objects(muow)
        assert total == 5

    async def test_update_mailing(self, muow):
        await update_object(muow, 1, MailingUpdate(message="updated mailing"))
        mailing: MailingORM = await get_object(muow, id=1)
        assert mailing.message == "updated mailing"

    async def test_get_mailing(self, muow):
        mailing: MailingORM = await get_object(muow, id=2)
        assert mailing.message == "test mailing №:2"

    async def test_get_all_mailings(self, muow):
        mailing: list = await get_all_objects(muow)
        total: int = len(mailing)
        assert total == 5

    async def test_delete_mailing(self, muow):
        await delete_object(muow, 1)
        total: int = await get_total_objects(muow)
        assert total == 4
        mailing: MailingORM = await get_object(muow, id=1)
        assert mailing is None
