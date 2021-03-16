from pydantic import BaseModel
from typing import List, Optional

class FileBase(BaseModel):
    filename: str

class File(FileBase):
    id: int
    file_name: str
    file_link: str
    created_at: str

class FileList(FileBase):
    files:Optional[File]

class FileCreate(FileBase):
    file_link:str

    class Config:
        orm_mode = True