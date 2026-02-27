import datetime

from fastapi import APIRouter

from app.fixtures.wrapper import fixtures_container

catalog_router = APIRouter(prefix="/catalogs", tags=["sync"])


@catalog_router.post('/')
async def fetch_catalogs_by_user() -> list:
    return fixtures_container.catalog_router__post__fetch_catalogs_by_user


@catalog_router.get('/content/{data_name}')
async def get_content_by_type(data_name: str) -> dict:
    fixtures_data = getattr(fixtures_container, f"catalog_router__get__get_content_by_type__{data_name}", [])
    return {
        "data_name": data_name,
        "synced_at": datetime.datetime.now(),
        "delta": fixtures_data,
        "limit": len(fixtures_data),
        "offset": 0,
        "total": len(fixtures_data),
    }
