import pytest
import sys
sys.path.append('c:\\Users\\Roman\\Desktop\\Project\\Mailing')
import asyncio

from database.config import settings
from database.engine import async_engine
from client.models import *
from tag.models import *
from mailing.models import *


@pytest.fixture(scope='session')
def event_loop():
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


@pytest.fixture(scope='session', autouse=True)
async def setup_db():
    assert settings.MODE == 'TEST'
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
        yield
        await conn.run_sync(Base.metadata.drop_all)
