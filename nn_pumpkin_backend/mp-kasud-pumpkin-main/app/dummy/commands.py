from fastapi import APIRouter

from app.fixtures.wrapper import fixtures_container

commands_router = APIRouter(tags=["sync"])

@commands_router.post('/decisions')
async def decide():
    return fixtures_container.commands_router__post__decisions
