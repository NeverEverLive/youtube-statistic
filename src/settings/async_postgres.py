from pydantic import BaseSettings
from pydantic import Field


class AsyncPGStorageSettings(BaseSettings):
    host: str = Field(env="PG_STORAGE_HOST", default="localhost")
    port: int = Field(env="PG_STORAGE_PORT", default=5432)
    username: str = Field(env="PG_STORAGE_USERNAME", default="postgres")
    password: str = Field(env="PG_STORAGE_PASSWORD", default="postgres")
    database: str = Field(env="PG_STORAGE_DATABASE", default="postgres")

    def geturl(self):
        return f"postgresql+asyncpg://{self.username}:{self.password}@{self.host}:{self.port}/{self.database}"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
