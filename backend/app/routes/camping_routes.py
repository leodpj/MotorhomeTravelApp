from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import models, schemas, database

router = APIRouter()

@router.post("/", response_model=schemas.Camping)
def create_camping(camping: schemas.CampingCreate, db: Session = Depends(database.get_db)):
    db_camping = models.Camping(**camping.dict())
    db.add(db_camping)
    db.commit()
    db.refresh(db_camping)
    return db_camping

@router.get("/{camping_id}", response_model=schemas.Camping)
def read_camping(camping_id: int, db: Session = Depends(database.get_db)):
    db_camping = db.query(models.Camping).filter(models.Camping.id == camping_id).first()
    if db_camping is None:
        raise HTTPException(status_code=404, detail="Camping não encontrado")
    return db_camping
