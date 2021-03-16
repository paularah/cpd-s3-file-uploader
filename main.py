from fastapi import FastAPI, File, UploadFile, Depends, HTTPException
from fastapi_sqlalchemy import DBSessionMiddleware
from pydantic import BaseModel 
from typing import Optional 
from routes import router
from settings import settings

app = FastAPI(title="Cloud patform development course", description="Simple S3 Buckets uploader")
app.add_middleware(DBSessionMiddleware,db_url=settings.SQLALCHEMY_DATABASE_URI)
app.include_router(router)