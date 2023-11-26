from datetime import datetime
from typing import Optional
from pydantic import BaseModel, EmailStr, Field, ConfigDict

from tag.schemas import TagGet


class ClientGet(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    email: str
    create_at: datetime
    update_at: datetime
    tags: list[TagGet] = Field(alias='tags_of_client', default=[])


class ClientCreate(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    email: EmailStr
    tags: list[TagGet] = Field(alias='tags_of_client', default=[])


class ClientUpdate(BaseModel):
    email: EmailStr
