from sqlalchemy.orm import Session
from app.models.npu import NPUCreation, Score
from app.schemas.npu import NPUCreationCreate, ScoreCreate

def create_npu(db: Session, npu: NPUCreationCreate, user_id: int):
    db_npu = NPUCreation(**npu.dict(), user_id=user_id, tags=",".join(npu.tags or []))
    db.add(db_npu)
    db.commit()
    db.refresh(db_npu)
    return db_npu

def add_score(db: Session, npu_id: int, score: ScoreCreate, user_id: int):
    db_score = Score(**score.dict(), npu_creation_id=npu_id, user_id=user_id)
    db.add(db_score)
    db.commit()
    db.refresh(db_score)
    return db_score

def search_by_tag(db: Session, tag: str):
    return db.query(NPUCreation).filter(NPUCreation.tags.ilike(f"%{tag}%")).all()
