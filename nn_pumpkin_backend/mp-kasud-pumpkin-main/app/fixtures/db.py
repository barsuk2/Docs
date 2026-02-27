from sqlmodel import Session
from app.db import engine
from app.dummy.repository import DemoUserCommandRepository, DemoUserQueryRepository
from app.settings import settings


def _init_database_fixtures(session: Session, force: bool):
    # -- Dependencies -- #
    demo_user_query_repository: DemoUserQueryRepository = DemoUserQueryRepository(session)
    demo_user_command_repository: DemoUserCommandRepository = DemoUserCommandRepository(session)
    
    # -- Force Behaviour -- #
    if force:
        demo_user_command_repository.drop_all()

    # -- Setting up Demo Users -- #
    for user_name in settings.ALLOWED_USERNAMES:
        existing_user = demo_user_query_repository.get_by_user_name(user_name)
        if existing_user:
            continue
        demo_user_command_repository.create(user_name=user_name, deactivated=False)
 
def init_fixtures(force=False):
    with Session(engine) as session:
        _init_database_fixtures(session, force) 



