from fastapi import APIRouter
from app.fixtures.wrapper import fixtures_container

config_router = APIRouter(prefix="/configs", tags=["configs"])

@config_router.get('/list_user_setting')
async def get_user_settings() -> dict:
    return fixtures_container.config_router__get__list_user_settings


@config_router.get('/{config_id}')
async def fetch_config_id():
    return fixtures_container.config_router__get__config_id


@config_router.get('/')
async def fetch_config():
    return fixtures_container.config_router__get


@config_router.post('/check_version')
async def check_version():
    return fixtures_container.config_router__post__check_version

@config_router.post('/user_setting')
async def user_settings():
    return fixtures_container.config_router__post__user_settings
