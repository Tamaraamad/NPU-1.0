from fastapi import APIRouter, HTTPException
from typing import Any, List
from sqlmodel import select

from app.api.deps import SessionDep, CurrentUser
from app.schemas.npu import  NPUCreation, NPUCreationCreate, NPUCreationPublic, Score, ScoreCreate,ScorePublic

router = APIRouter(prefix="/npu", tags=["npu"])

@router.post("/", response_model=NPUCreationPublic)
def create_npu(
    *, session: SessionDep, current_user: CurrentUser, npu_in: NPUCreationCreate
) -> Any:
    npu = NPUCreation.model_validate(npu_in, update={"user_id": current_user.id})
    session.add(npu)
    session.commit()
    session.refresh(npu)
    return npu

@router.post("/{npu_id}/score", response_model=ScorePublic)
def score_npu(
    *, session: SessionDep, current_user: CurrentUser, npu_id: int, score_in: ScoreCreate
) -> Any:
    score = Score.model_validate(score_in, update={"user_id": current_user.id, "npu_creation_id": npu_id})
    session.add(score)
    session.commit()
    session.refresh(score)
    return score

@router.get("/search", response_model=List[NPUCreationPublic])
def search_npu_by_tag(tag: str, session: SessionDep) -> Any:
    statement = select(NPUCreation).where(NPUCreation.tags.ilike(f"%{tag}%"))
    results = session.exec(statement).all()
    return results
