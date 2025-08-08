from pydantic import BaseModel
from typing import Optional, List

class ScoreCreate(BaseModel):
    creativity: int
    uniqueness: int

class Score(BaseModel):
    id: int
    creativity: int
    uniqueness: int
    user_id: int

    class Config:
        orm_mode = True

class NPUCreationBase(BaseModel):
    title: str
    description: Optional[str]
    image_url: Optional[str]
    tags: Optional[List[str]]

class NPUCreationCreate(NPUCreationBase):
    pass

class NPUCreation(NPUCreationBase):
    id: int
    user_id: int
    scores: List[Score] = []

    class Config:
        orm_mode = True

class ScorePublic(ScoreCreate):
    id: int
    user_id: int
    npu_creation_id: int

    class Config:
        orm_mode = True


class NPUCreation(BaseModel):
    id: int
    user_id: int
    title: str
    description: Optional[str]
    image_url: Optional[str]
    tags: Optional[List[str]]
    scores: List[ScorePublic] = []

    class Config:
        orm_mode = True


class NPUCreationPublic(NPUCreation):
    pass



