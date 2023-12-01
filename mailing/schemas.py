from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict, Field

from tag.schemas import TagGet


class MailingCreate(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    start: Optional[datetime] = None
    message: str
    tags: list[str] = Field(alias="tags_of_mailing", default=[])


class MailingGet(MailingCreate):
    id: int
    create_at: datetime
    tags: list[TagGet] = Field(alias="tags_of_mailing", default=[])


class MailingUpdate(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    start: Optional[datetime] = None
    message: Optional[str] = None
