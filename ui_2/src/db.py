from typing import Optional
import uuid
from sqlmodel import Field, Session, SQLModel, create_engine, select


class Hero(SQLModel, table=True):
    id: Optional[str] = Field(str(uuid.uuid4()), primary_key=True)
    name: str
    secret_name: str
    age: Optional[int] = None


engine = create_engine("sqlite:///database.db")

def create_hero(data):
    with Session(engine) as session:
        session.add(data)
        session.commit()

def get_hero_id(id):
    with Session(engine) as session:
        statement = select(Hero).where(Hero.id == id)
        hero = session.exec(statement).first()
        print(hero)

if __name__ == "__main__":
    hero = [Hero(name="Deadpond", secret_name="Dive Wilson"),Hero(name="Spider-Boy", secret_name="Pedro Parqueador"),Hero(name="Rusty-Man", secret_name="Tommy Sharp", age=48)]
    for h in hero:
        create_hero(data=h)
        get_hero_id(h.id)