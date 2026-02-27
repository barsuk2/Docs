from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DEBUG: bool = False
    PROJECT_NAME: str = "KASUD Backend Pumpkin (dummy)"
    PROJECT_DESCRIPTION: str = "Dummy copy of KASUD Application service to use while reviewing mobile application"

    ALLOWED_USERNAMES: list[str] = ["test_user", "reviewer", "demo_user"]

    class Config:
        env_file = (".env", "tests/testing.env")
        case_sensitive = True


settings = Settings()
