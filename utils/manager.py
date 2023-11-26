from sqlalchemy import select, insert, update, delete, func
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Union, ClassVar
from sqlalchemy.exc import NoResultFound
from abc import ABC, abstractclassmethod


class ABCObjectManager(ABC):
    @abstractclassmethod
    async def get(self, **kwargs):
        ...
    @abstractclassmethod
    async def all(self):
        ...
    @abstractclassmethod
    async def create(self, **kwargs):
        ...
    @abstractclassmethod
    async def update(self, obj_id, **kwargs):
        ...
    @abstractclassmethod
    async def delete(self, **kwargs):
        ...
    @abstractclassmethod
    async def get_or_create(self, **kwargs):
        ...
    @abstractclassmethod
    async def count(self):
        ...
    


class ObjectManager(ABCObjectManager):
    
    def __init__(self, session: AsyncSession):
        self.session = session
    
    async def get(self, **kwargs):
        """
        Возвращает объект таблицы.
        Если объект не найден, возвращает None.
        kwargs: Данные для поиска объекта.
        """
        query = select(self.model).filter_by(**kwargs)
        result = await self.session.execute(query)
        return result.scalar_one_or_none()

    async def all(self):
        """
        Возвращает список всех объектов таблицы.
        """
        query = select(self.model).order_by(self.model.id)
        result = await self.session.execute(query)
        return result.scalars().all()

    async def create(self, **kwargs):
        """
        Создает объект таблицы.
        Возвращает объект, при возникновении ошибки вернет None.
        Не сохраняет изменения в базе данных.
        kwargs: Данные для создания объекта.
        """
        stmt = insert(self.model).values(**kwargs).returning(self.model)
        result = await self.session.execute(stmt)
        return result.scalar_one_or_none()

    async def update(self, obj_id, **kwargs):
        """
        Обновляет данные объекта.
        Возвращает объект при успешнои обновлении и None
        при откате. 
        Не сохраняет изменения в базе данных.
        filter: dict -  Данные для поиска объекта (id=1 | name='Roman')
        kwargs: Новые данные.
        """
        stmt = update(self.model).filter_by(id=obj_id).values(**kwargs).returning(self.model)
        result = await self.session.execute(stmt)
        return result.scalar_one_or_none()
            

    async def delete(self, **kwargs):
        """
        Удаляет объект из таблицы.
        Возвращает True при успешнои удалении и False 
        при откате.
        Не сохраняет изменения в базе данных.
        kwargs: Данные для поиска объекта
        """
        stmt = delete(self.model).filter_by(**kwargs)
        result = await self.session.execute(stmt)
        return bool(result.unique().rowcount)

    async def get_or_create(self, **kwargs):
        """
        Возвращает имеющийся, или, при отсутствии, создает и возвращает
        объект таблицы.
        Не сохраняет изменения в базе данных.
        kwargs: Данные для поиска/создания объекта.
        """
        result = await self.get(**kwargs)
        if not result:
            result = await self.create(**kwargs)
        return result

    async def count(self):
        """
        Возвращает общее числовое количество объектов в таблице.
        """
        query = select(func.count(self.model.id)).select_from(self.model)
        result = await self.session.execute(query)
        return result.scalar_one()
