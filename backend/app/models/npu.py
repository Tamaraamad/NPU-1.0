from typing import Optional, List
from pydantic import BaseModel


# ---------- Score Schemas ----------

class ScoreCreate(BaseModel):
    creativity: int
    uniqueness: int


class ScorePublic(ScoreCreate):
    id: int
    user_id: int
    npu_creation_id: int

    class Config:
        orm_mode = True


# ---------- NPU Creation Schemas ----------

class NPUCreationBase(BaseModel):
    title: str
    description: Optional[str]
    image_url: Optional[str]
    tags: Optional[List[str]]


class NPUCreationCreate(NPUCreationBase):
    pass


class NPUCreationPublic(NPUCreationBase):
    id: int
    user_id: int
    scores: List[ScorePublic] = []

    class Config:
        orm_mode = True




