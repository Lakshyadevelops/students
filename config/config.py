from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    DATABASE_URI: str
    DATABASE_STUDENTS: str

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()
