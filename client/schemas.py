from datetime import datetime

from pydantic import BaseModel, ConfigDict, EmailStr, Field

from tag.schemas import TagGet


class ClientCreate(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    email: EmailStr
    tags: list[str] = Field(alias="tags_of_client", default=[])


class ClientGet(ClientCreate):
    id: int
    create_at: datetime
    update_at: datetime
    tags: list[TagGet] = Field(alias="tags_of_client", default=[])


class ClientUpdate(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    email: EmailStr
