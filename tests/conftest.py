import asyncio
import pytest
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parents[1]))

from client.models import ClientORM
from database.config import settings
from database.engine import Base, async_engine
from mailing.models import MailingORM
from utils.unitofwork import ABCUnitOfWork, UnitOfWork


@pytest.fixture(scope="session")
def event_loop():
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


@pytest.fixture(scope="session", autouse=True)
async def setup_db():
    assert settings.MODE == "TEST"
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
        yield
        await conn.run_sync(Base.metadata.drop_all)


@pytest.fixture(scope="session", autouse=True)
def cuow():
    uow: ABCUnitOfWork = UnitOfWork(ClientORM)
    return uow


@pytest.fixture(scope="session", autouse=True)
def muow():
    uow: ABCUnitOfWork = UnitOfWork(MailingORM)
    return uow
