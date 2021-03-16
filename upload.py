
from botocore.exceptions import ClientError


def upload_file_to_bucket(s3_client, file_obj, bucket, folder, object_name=None):
    # If S3 object_name was not specified, use file_name
    if object_name is None:
        object_name = file_obj
    # Upload the file
    try:
        s3_client.upload_fileobj(file_obj, bucket, f"{folder}/{object_name}")
    except ClientError as e:
        print(e)
        return False
    return True