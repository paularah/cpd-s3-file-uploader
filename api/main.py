from fastapi import FastAPI, File, UploadFile, Depends, HTTPException
import models, schema, controller
from db import engine, SessionLocal
from sqlalchemy.orm import Session
from pydantic import BaseModel 
from typing import Optional 
from dotenv import load_dotenv

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
load_dotenv(os.path.join(BASE_DIR, ".env"))

models.Base.metadata.create_all(bind=engine)

# dependecy injection
def get_db():
    db = None
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()

app = FastAPI()

@app.get('/')
def read_root():
    return {'greetinngs':'welcometo my fast apu'}

@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile = File(...)):
    return {"filename": file.filename}

@app.get('/file{id}')
async def get_file(id:str, db: Session = Depends(get_db)):
    a_file = controller.get_file_by_id(db, id)
    if not a_file:
        raise HTTPException(status_code=400, detail="could not find a file with this ID")
    return a_file

@app.get('files')
async def get_all_files(db: Session = Depends(get_db)):
    all_files = controller.get_all_s3_files(db)
    if not all_files:
        raise HTTPException(status_code=400, detail="could not get files")
    return all_files