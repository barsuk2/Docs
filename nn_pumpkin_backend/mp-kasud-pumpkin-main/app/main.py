from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.db import create_db
from app.dummy.commands import commands_router
from app.fixtures.db import init_fixtures
from app.settings import settings

from app.dummy.config import config_router
from app.dummy.auth import auth_router
from app.dummy.sync import sync_router
from app.dummy.catalogs import catalog_router


def create_app() -> FastAPI:
    app = FastAPI(
        title=settings.PROJECT_NAME,
        description=settings.PROJECT_DESCRIPTION,
        docs_url="/",
        version="1",
        dependencies=[],
    )

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.include_router(config_router)
    app.include_router(auth_router)
    app.include_router(sync_router)
    app.include_router(catalog_router)
    app.include_router(commands_router)

    create_db()
    init_fixtures()
    return app


app = create_app()
