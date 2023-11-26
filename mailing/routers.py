from typing import Union

from fastapi import APIRouter
from utils.services import (create_object, update_object,
                            delete_object, get_all_objects, get_object, add_tag, del_tag)
from utils.unitofwork import ABCUnitOfWork, UnitOfWork

from mailing.schemas import MailingCreate, MailingGet, MailingUpdate
from mailing.responses import ResponsMailing
from mail.sending import send_message
from tag.schemas import TagCreate
from client.relevant_clients import get_relevant_clients
from logs.config import mailinglog
from mailing.models import MailingORM


router = APIRouter(prefix='/mailing', tags=['Mailing'])
uow: ABCUnitOfWork = UnitOfWork(MailingORM)
response: ResponsMailing = ResponsMailing()


@router.get(
    '/all',
    response_model=list[MailingGet],
    response_model_by_alias=False,
    summary='Получить список рассылок'
)
async def get_all_malings():
    mailing = await get_all_objects(uow)
    return mailing


@router.get(
    '/{mailing_id}',
    response_model=Union[MailingGet, dict[str, str]],
    response_model_by_alias=False,
    summary='Получить данные рассылки',
)
async def get_mailing(mailing_id: int):
    mailing = await get_object(uow, id=mailing_id)
    if not mailing:
        return response.not_found
    return mailing


@router.post(
    '/create',
    response_model=Union[MailingGet, dict[str, str]],
    response_model_by_alias=False,
    summary='Создать новую рассылку',
)
async def create_mailing(data: MailingCreate):
    mailinglog.info('Запрос на запись новой рассылки.')
    mailing = await create_object(uow, data)
    if not mailing:
        return response.unique_error
    mailinglog.info('Рассылка создана.')
    clients = await get_relevant_clients(mailing.tags_of_mailing)
    mailinglog.info('Начало работы send_massege.')
    send_message.apply_async((mailing.message, clients), eta=mailing.start)
    return mailing


@router.patch(
    '/update/{mailing_id}',
    response_model=Union[MailingGet, dict[str, str]],
    response_model_by_alias=False,
    summary='Обновить данные рассылки',
)
async def update_mailing(mailing_id: int, data: MailingUpdate):
    mailing = await create_or_update_object(uow, data, mailing_id)
    if not mailing:
        return response.not_found
    return mailing


@router.delete(
    '/delete/{mailing_id}',
    response_model=dict[str, str],
    response_model_by_alias=False,
    summary='Удалить рассылку',
)
async def delete_mailing(mailing_id: int):
    mailing = await delete_object(uow, mailing_id)
    if not mailing:
        return response.not_found
    return response.deleted


@router.post(
    '/{obj_id}/add',
    response_model=dict[str, str],
    response_model_by_alias=False,
    summary='Добавить тег клиенту',
)
async def add_teg(obj_id: int, tags: TagCreate):
    mailing = await add_tag(uow, obj_id, tags)
    if not mailing:
        return response.not_found
    return mailing


@router.delete(
    '/{obj_id}/del',
    response_model=dict[str, str],
    response_model_by_alias=False,
    summary='Удалить тег клиента',
)
async def delete_tag(obj_id: int, tag_id: int):
    mailing = await del_tag(uow, obj_id, tag_id)
    if not mailing:
        return response.not_found
    return mailing
