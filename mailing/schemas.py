from pydantic import BaseModel, Field, ConfigDict
from datetime import datetime, timezone
from typing import Optional, Annotated
from sqlalchemy import text

from tag.schemas import TagGet


class MailingGet(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    start: datetime
    message: str
    create_at: datetime
    tags: list[TagGet] = Field(alias='tags_of_mailing', default=[])


class MailingCreate(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    start: Optional[datetime] = None
    message: str
    tags: list = Field(alias='tags_of_mailing', default=[])


class MailingUpdate(BaseModel):
    start: Optional[datetime] = None
    message: Optional[str] = None
