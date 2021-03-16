from pydantic import BaseSettings

class Settings(BaseSettings):
    AWS_BUCKET_NAME:str
    AWS_ACCESS_ID:str
    SQLALCHEMY_DATABASE_URI:str
    AWS_SECRET_ACCESS_KEY:str

    class Config:
        env_file = ".env"


settings = Settings(_env_file='.env')