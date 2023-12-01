from sqlalchemy import select

from client.models import ClientORM, ClientTagORM
from logs.config import mailinglog
from utils.unitofwork import ABCUnitOfWork, UnitOfWork

uow: ABCUnitOfWork = UnitOfWork(ClientORM)


async def get_relevant_clients(tags):
    tags_id = []
    for tag in tags:
        tags_id.append(tag.id)
    mailinglog.info("ID тегов поулчены.")
    async with uow:
        subquery = select(ClientTagORM.obj_id).where(
            ClientTagORM.tag_id.in_((tags_id))
        )
        query = select(ClientORM.email).where(ClientORM.id.in_(subquery))
        emails = await uow.execute(query)
        mailinglog.info(
            "Запрос на подходящих пользователей выполнен. " "Кленты получены."
        )
        emails = emails.scalars().all()
        mailinglog.info(f"{emails}")
        return emails
