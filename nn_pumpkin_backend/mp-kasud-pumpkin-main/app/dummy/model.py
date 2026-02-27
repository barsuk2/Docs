from sqlmodel import Field, SQLModel


class DemoUser(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    user_name: str
    deactivated: bool
