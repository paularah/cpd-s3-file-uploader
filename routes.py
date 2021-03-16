from botocore.client import BaseClient
from fastapi import APIRouter, Depends, HTTPException, status, File, UploadFile
from fastapi.responses import JSONResponse
from s3 import s3_auth
from upload import upload_file_to_s3
from settings import settings
from schema import FileList
from controller import get_all_files

router = APIRouter()

@router.post("/upload", status_code=status.HTTP_201_CREATED, summary="Upload files to AWS S3 Buckets",
             description="Upload a file to AWS S3 bucket", name="UPLOAD file to AWS S3",
             response_description="uploaded file successfully")
async def upload_file(folder: str, s3: BaseClient = Depends(s3_auth), file_obj: UploadFile = File(...)):
    upload_obj = await upload_file_to_s3(s3_client=s3, file_obj=file_obj.file,
                                       bucket=settings.AWS_BUCKET_NAME,
                                       folder=folder,
                                       object_name=file_obj.filename
                                       )

    if upload_obj:
        return JSONResponse(content="File has been uploaded to bucket successfully",
                            status_code=status.HTTP_201_CREATED)
    else:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                            detail="File could not be uploaded")


@router.get("/files",  description="returns all files in the database", name="GET files from db")
async def get_files():
   all_files =  await get_all_files()
   if all_files:
       return all_files
   else:
        raise HTTPException(status_code=status.HTTP_400_NOT_FOUND,
                            detail="could not get files")
