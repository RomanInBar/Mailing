from client.schemas import ClientGet
from mailing.schemas import MailingGet
from tag.schemas import TagCreate, TagGet
from utils.services import add_tag, del_tag


class TestOfTag:
    async def test_add_tag_client(self, client):
        tags = TagCreate(name=["white", "blue", "red"])
        uow, client = client
        client = await add_tag(uow, client.id, tags)
        data = ClientGet.model_validate(client)
        assert data.tags == [
            TagGet(id=1, name="white"),
            TagGet(id=2, name="blue"),
            TagGet(id=3, name="red"),
        ]

    async def test_remove_tag_client(self, client):
        uow, client = client
        client = await del_tag(uow, client.id, 1)
        data = ClientGet.model_validate(client)
        assert data.tags == [
            TagGet(id=2, name="blue"),
            TagGet(id=3, name="red"),
        ]

    async def test_add_tag_mailing(self, mailing):
        tags = TagCreate(name=["white", "blue", "red"])
        uow, mailing = mailing
        mailing = await add_tag(uow, mailing.id, tags)
        data = MailingGet.model_validate(mailing)
        assert data.tags == [
            TagGet(id=1, name="white"),
            TagGet(id=2, name="blue"),
            TagGet(id=3, name="red"),
        ]

    async def test_remove_tag_mailing(self, mailing):
        uow, mailing = mailing
        mailing = await del_tag(uow, mailing.id, 1)
        data = MailingGet.model_validate(mailing)
        assert data.tags == [
            TagGet(id=2, name="blue"),
            TagGet(id=3, name="red"),
        ]
