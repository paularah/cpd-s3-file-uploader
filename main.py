from fastapi import FastAPI, File, UploadFile, Depends, HTTPException
import models, schema, controller
from db import engine, SessionLocal
from sqlalchemy.orm import Session
from pydantic import BaseModel 
from typing import Optional 
from dotenv import load_dotenv

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
load_dotenv(os.path.join(BASE_DIR, ".env"))


app = FastAPI()

