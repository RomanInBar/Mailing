from pydantic import BaseModel

from utils.unitofwork import ABCUnitOfWork


async def get_all_objects(uow: ABCUnitOfWork):
    """
    Возвращает список всех объектов таблицы.
    uow: ABCUnitOfWork - кастомный контекстный менеджер.
    """
    async with uow:
        subject = await uow.objects.all()
        return subject


async def get_object(uow: ABCUnitOfWork, **kwargs):
    """
    Возвращает объект таблицы.
    uow: ABCUnitOfWork - кастомный контекстный менеджер.
    kwargs: Данные для поиска объекта.
    """
    async with uow:
        subject = await uow.objects.get(**kwargs)
        return subject


async def create_object(uow: ABCUnitOfWork, data: BaseModel):
    """
    Создает новый объект в таблице.
    uow: ABCUnitOfWork - кастомный контекстный менеджер.
    data: BaseModel pydantic scheme - данные объекта.
    """
    data = data.model_dump()
    tags = data.pop("tags")
    async with uow:
        subject = await uow.objects.create(**data)
        for tag in tags:
            tag = await uow.tags.get_or_create(name=tag)
            subject.append_tag(tag)
        await uow.commit()
        return subject


async def update_object(uow: ABCUnitOfWork, obj_id: int, data: BaseModel):
    """
    Обновляет данные объекта.
    Сохраняет изменения в базе данных.
    Возвращает объект.
    uow: ABCUnitOfWork - кастомный контекстный менеджер.
    obj_id: int - ID объекта.
    data: BaseModel pydantic scheme - новые данные.
    """
    data = data.model_dump(exclude_none=True)
    async with uow:
        subject = await uow.objects.update(obj_id, **data)
        await uow.commit()
        return subject


async def delete_object(uow: ABCUnitOfWork, obj_id: int):
    """
    Удаляет объект из таблицы.
    Сохраняет изменения в базе данных.
    Возвращает объект.
    uow: ABCUnitOfWork - кастомный контекстный менеджер.
    obj_id: int - ID объекта.
    """
    async with uow:
        result = await uow.objects.delete(id=obj_id)
        await uow.commit()
        return result


async def add_tag(uow: ABCUnitOfWork, obj_id: int, tags: BaseModel):
    """
    Добавляет тег к объекту.
    Если изначальный объект не найдет, возвращает None,
    при успешном добавлении возвращает объект.
    Сохраняет изменения в базе данных.
    uow: ABCUnitOfWork - кастомный контекстный менеджер.
    obj_id: int - ID объекта.
    tags: BaseModel pydantic scheme - добавленные теги.
    """
    async with uow:
        subject = await uow.objects.get(id=obj_id)
        tags = tags.model_dump().pop("name")
        for tag in tags:
            tag = await uow.tags.get_or_create(name=tag)
            subject.append_tag(tag)
        await uow.commit()
        return subject


async def del_tag(uow: ABCUnitOfWork, obj_id: int, tag_id: int):
    """
    Удаляет тег обекта.
    Если изначальный объект не найден, возвращает None, при
    успешном удалении возвращает объект.
    Сохраняет изменения в базе данных.
    uow: ABCUnitOfWork - кастомный контекстный менеджер.
    obj_id: int - ID объекта.
    tag_id: int - ID тега.
    """
    async with uow:
        subject = await uow.objects.get(id=obj_id)
        tag = await uow.tags.get(id=tag_id)
        subject.remove_tag(tag)
        await uow.commit()
        return subject


async def get_total_objects(uow: ABCUnitOfWork):
    """
    Возвращает общее числовое количество объектов в таблице.
    uow: ABCUnotOfWork - кастомный контекстный менеджер.
    """
    async with uow:
        total = await uow.objects.count()
        return total
