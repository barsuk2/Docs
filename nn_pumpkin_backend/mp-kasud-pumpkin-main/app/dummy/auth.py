from copy import copy
from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse
from app.di import DBSession
from app.dummy.repository import DemoUserCommandRepository, DemoUserQueryRepository
from app.fixtures.wrapper import fixtures_container

auth_router = APIRouter(prefix="/auth", tags=["configs"])


@auth_router.post("/login")
async def login_user(request: Request, db_session: DBSession):
    demo_user_query_repository: DemoUserQueryRepository = DemoUserQueryRepository(db_session)

    json_body = await request.json()
    login = json_body.get("login")

    found_user = demo_user_query_repository.get_by_user_name(login)
    if found_user and not found_user.deactivated:
        fixtures_data = copy(fixtures_container.auth_router__post__login)
        fixtures_data["token"] += f"==={login}"
        return fixtures_data

    return JSONResponse(
        status_code=404,
        content={
            "status": "error",
            "message": "Пользователь не найден",
            "user_message": "Пользователь не найден",
        },
    )


@auth_router.post("/check")
async def check():
    return fixtures_container.auth_router__post__login


@auth_router.post("/logout")
async def logout(request: Request, db_session: DBSession):
    demo_user_command_repository: DemoUserCommandRepository = DemoUserCommandRepository(db_session)
    demo_user_query_repository: DemoUserQueryRepository = DemoUserQueryRepository(db_session)

    json_body = await request.json()
    delete_account = json_body.get("deleteAccount")
    token_header = request.headers.get("user-token")
    print(json_body)

    if delete_account and token_header:
        user_name = token_header.split("===")[-1]

        if not user_name:
            return fixtures_container.auth_router__post__logout

        user = demo_user_query_repository.get_by_user_name(user_name)
        if not user:
            return fixtures_container.auth_router__post__logout

        demo_user_command_repository.deactivate_user(user.user_name)

    return fixtures_container.auth_router__post__logout

