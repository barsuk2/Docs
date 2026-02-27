from dataclasses import dataclass
from sqlalchemy import ScalarResult
from sqlmodel import Session, delete, select, update

from app.dummy.model import DemoUser

@dataclass
class BaseRepository:
    session: Session

    def commit(self):
        self.session.commit()

class DemoUserQueryRepository(BaseRepository):

    def get_by_user_name(self, user_name: str) -> DemoUser | None:
        return self.session.exec(select(DemoUser).where(DemoUser.user_name == user_name)).first()

    def find_by(self, **kwargs) -> ScalarResult[DemoUser]:
        return self.session.exec(select(DemoUser))


class DemoUserCommandRepository(BaseRepository):
    
    def create(self, **kwargs) -> DemoUser:
        user = DemoUser(**kwargs)
        self.session.add(user)
        self.commit()
        return user

    def drop_all(self):
        self.session.execute(delete(DemoUser))
        self.session.commit()

    def deactivate_user(self, user_name: str):
        self.session.execute(update(DemoUser).where(DemoUser.user_name == user_name).values(deactivated=True))
        self.session.commit()
