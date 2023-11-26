from typing import Union

from fastapi import APIRouter

from client.schemas import ClientCreate, ClientGet, ClientUpdate
from utils.services import (
    create_object,
    delete_object,
    get_all_objects,
    get_object,
    update_object,
    add_tag,
    del_tag,
)
from client.responses import ResponsClient
from utils.unitofwork import UnitOfWork, ABCUnitOfWork
from tag.schemas import TagCreate

from client.models import ClientORM


router = APIRouter(prefix='/client', tags=['Client'])
cuow: ABCUnitOfWork = UnitOfWork(ClientORM)
response: ResponsClient = ResponsClient()


@router.get(
    '/all',
    response_model=list[ClientGet],
    response_model_by_alias=False,
    summary='Получить список клиентов',
)
async def get_all_clients():
    clients = await get_all_objects(uow)
    return clients


@router.get(
    '/{user_id}',
    response_model=Union[ClientGet, dict[str, str]],
    response_model_by_alias=False,
    summary='Получить данные клиента',
)
async def get_client(user_id: int):
    client = await get_object(uow, id=user_id)
    if not client:
        return response.not_found
    return client


@router.post(
    '/create',
    response_model=Union[ClientGet, dict[str, str]],
    response_model_by_alias=False,
    summary='Создать нового клиента',
)
async def create_client(data: ClientCreate):
    client = await create_object(uow, data)
    if not client:
        return response.unique_error
    return client


@router.patch(
    '/update/{user_id}',
    response_model=Union[ClientGet, dict[str, str]],
    response_model_by_alias=False,
    summary='Обновить данные клиента',
)
async def update_client(user_id: int, data: ClientUpdate):
    client = await update_object(uow, user_id, data)
    if not client:
        return response.not_found
    return client


@router.delete(
    '/delete/{user_id}',
    response_model=dict[str, str],
    summary='Удалить данные клиента',
)
async def delete_client(user_id: int):
    client = await delete_object(uow, user_id)
    if client:
        return response.deleted
    return response.not_found


@router.post(
    '/{obj_id}/add',
    response_model=dict[str, str],
    response_model_by_alias=False,
    summary='Добавить тег клиенту',
)
async def add_teg(obj_id: int, tags: TagCreate):
    client = await add_tag(uow, obj_id, tags)
    if not client:
        return response.not_found
    return client


@router.delete(
    '/{obj_id}/del',
    response_model=dict[str, str],
    response_model_by_alias=False,
    summary='Удалить тег клиента',
)
async def delete_tag(obj_id: int, tag_id: int):
    client = await del_tag(uowr, obj_id, tag_id)
    if not client:
        return response.not_found
    return client
