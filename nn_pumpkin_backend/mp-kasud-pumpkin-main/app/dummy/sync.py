from fastapi import APIRouter, Request

from app.fixtures.wrapper import fixtures_container

sync_router = APIRouter(tags=["sync"])

@sync_router.post('/sync')
async def sync(request: Request):
    json_body = await request.json()
    data_key = json_body["data_key"]
    is_required = json_body.get("is_required", True)

    fixtures_data = getattr(fixtures_container, f"sync_router__post__{data_key}", None)
    if data_key == "tasks" and not is_required:
        fixtures_data = fixtures_container.sync_router__post__tasks__not_required

    if not fixtures_data:
        return fixtures_container.sync_router__post__default_sync

    return fixtures_data


@sync_router.post('/sync/content')
async def sync_content():
    return fixtures_container.sync_router__post__content

@sync_router.post('/sync/content/optional')
async def sync_content_optional(request: Request):
    print(await request.json())
    return fixtures_container.sync_router__post__content_optional



