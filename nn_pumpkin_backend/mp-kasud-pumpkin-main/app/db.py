from sqlmodel import SQLModel, create_engine

engine = create_engine("postgresql://postgres:postgres@db:5432/postgres")

def create_db():
    SQLModel.metadata.create_all(engine)

