from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from app import crud, models, schemas
from app.api import deps

router = APIRouter()

@router.post("/", response_model=schemas.NPUCreation)
def create_npu(
    npu: schemas.NPUCreationCreate,
    db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(deps.get_current_active_user),
):
    return crud.crud_npu.create_npu(db=db, npu=npu, user_id=current_user.id)

@router.post("/{npu_id}/score", response_model=schemas.Score)
def score_npu(
    npu_id: int,
    score: schemas.ScoreCreate,
    db: Session = Depends(deps.get_db),
    current_user: models.User = Depends(deps.get_current_active_user),
):
    return crud.crud_npu.add_score(db=db, npu_id=npu_id, score=score, user_id=current_user.id)

@router.get("/search", response_model=List[schemas.NPUCreation])
def search_npu_by_tag(
    tag: str,
    db: Session = Depends(deps.get_db),
):
    return crud.crud_npu.search_by_tag(db=db, tag=tag)
