from pydantic import BaseModel

class FileBase(BaseModel):
    filename: str

class FileCreate(UserBase):
    id: int
    file_name: str
    file_link: str
    created_at: str

class User(UserBase):
    id: int
    
    class Config:
        orm_mode = True