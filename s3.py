import boto3
from botocore.client import BaseClient

from settings import settings


def s3_auth() -> BaseClient:
    s3 = boto3.client(service_name='s3', aws_access_key_id=settings.AWS_ACCESS_ID,
                      aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY
                      )
    return s3