from abc import ABC, abstractmethod
from typing import Type

from sqlalchemy.ext.asyncio import AsyncSession

from database.engine import async_session_maker
from utils.manager import ABCObjectManager
from utils.repositories import Repository, TagRepository


class ABCUnitOfWork(ABC):
    objects: Type[ABCObjectManager]
    tags: Type[ABCObjectManager]

    @abstractmethod
    def __init__(self):
        ...

    @abstractmethod
    def __aenter__(self):
        ...

    @abstractmethod
    def __aexit__(self, *args):
        ...

    @abstractmethod
    def commit(self):
        ...

    @abstractmethod
    def rollback(self):
        ...

    @abstractmethod
    def add(self):
        ...


class UnitOfWork(ABCUnitOfWork):
    def __init__(self, model):
        self.session_factory: AsyncSession = async_session_maker
        self.model = model

    async def __aenter__(self):
        self.session = self.session_factory()
        self.objects = Repository(self.session)
        self.objects.model = self.model
        self.tags = TagRepository(self.session)

    async def __aexit__(self, *args):
        await self.session.close()

    async def commit(self):
        await self.session.commit()

    async def rollback(self):
        await self.session.rollback()

    async def add(self, obj):
        await self.session.add(obj)

    async def execute(self, query):
        result = await self.session.execute(query)
        return result
