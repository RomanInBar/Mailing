from pydantic import BaseModel, ConfigDict


class TagGet(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str


class TagCreate(BaseModel):
    name: list[str]
