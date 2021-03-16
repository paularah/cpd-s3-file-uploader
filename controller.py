from model import Files as FilesModel
from fastapi_sqlalchemy import db


async def save_upload(filename:str, filelink):
    File = FilesModel(filename=filename, filelink=filelink)
    db.session.add(File)
    db.session.commit()
    db.session.refresh(File)
    print('file succefully saved to db')

async def get_all_files():
     all_files = db.session.query(FilesModel).all()
     return all_files
