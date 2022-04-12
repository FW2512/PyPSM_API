from pydantic import BaseSettings

class Settings(BaseSettings):
    database_host_url: str
    database_port: str
    database_name: str
    database_user: str
    database_password: str
    secret_key: str
    algorithm: str
    expiration_time: int

    class Config:
        env_file = ".env"

settings = Settings()