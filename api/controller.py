from sqlalchemy.orm import Session
from . import models, schemas

def get_file_by_id(db: Session, id: str):
    return db.query(models.FileInfo).filter(models.FileInfo.id == id).first()