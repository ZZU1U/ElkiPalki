from datetime import datetime
from typing import Annotated
from sqlalchemy import ForeignKey, select
from sqlalchemy.orm import Mapped, mapped_column, relationship, selectinload
from .database import Base, session_factory
from .crud import CRUD
from .enums import Role, AnimalStatus


intpk = Annotated[int, mapped_column(primary_key=True)]


class User(Base, CRUD):
    __tablename__ = "user"
    id: Mapped[intpk]
    name: Mapped[str] = mapped_column(unique=True)
    phone: Mapped[str | None]
    role: Mapped[Role]
    walks: Mapped[list["Walk"]] = relationship(lazy='selectin')


class Walk(Base, CRUD):
    __tablename__ = "walk"
    id: Mapped[intpk]
    date: Mapped[datetime]
    duration: Mapped[int]
    animal_id: Mapped[int] = mapped_column(ForeignKey("animal.id"))
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    animal: Mapped["Animal"] = relationship(back_populates='walks', lazy='selectin')
    user: Mapped["User"] = relationship(back_populates='walks', lazy='selectin')

    @classmethod
    async def all(cls):
        async with session_factory() as session:
            stmt = select(cls).join(Animal, cls.animal_id == Animal.id)
            return (await session.execute(stmt)).unique().scalars().all()


class Animal(Base, CRUD):
    __tablename__ = "animal"
    id: Mapped[intpk]
    name: Mapped[str]
    species: Mapped[str]
    age: Mapped[int]
    description: Mapped[str]
    image: Mapped[str | None]
    status: Mapped[AnimalStatus] = mapped_column(default=AnimalStatus.available)
    last_donation: Mapped[datetime | None]
    food_donated: Mapped[int | None] = mapped_column(default=0)
    food_daily: Mapped[int | None] = mapped_column(default=500)
    walks: Mapped[list["Walk"]] = relationship(lazy='selectin')

    @classmethod
    async def all(cls):
        async with session_factory() as session:
            stmt = (
                select(cls)
            )
            return (await session.execute(stmt)).unique().scalars().all()
