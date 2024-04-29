from fastapi import Depends

from fastapi_users.db import SQLAlchemyBaseUserTable

from fastapi_users_db_sqlalchemy import SQLAlchemyUserDatabase
from fastapi_users_db_sqlalchemy.access_token import (
    SQLAlchemyAccessTokenDatabase,
    SQLAlchemyBaseAccessTokenTable,
)

from sqlalchemy import Integer, ForeignKey
from sqlalchemy.orm import declared_attr, Mapped, mapped_column, relationship
from sqlalchemy.ext.asyncio import AsyncSession

from pawapi.db.database import get_session, Base
from pawapi.db.annotations import intpk


class User(SQLAlchemyBaseUserTable[int], Base):
    __tablename__ = "user"
    id: Mapped[intpk]
    name: Mapped[str]
    is_volunteer: Mapped[bool] = mapped_column(default=False)
    phone: Mapped[str | None] = mapped_column(unique=True)
    walks: Mapped[list["Walk"]] = relationship(lazy='selectin')


class AccessToken(SQLAlchemyBaseAccessTokenTable[int], Base):
    @declared_attr
    def user_id(cls) -> Mapped[int]:
        return mapped_column(Integer, ForeignKey("user.id", ondelete="cascade"), nullable=False)


async def get_user_db(session: AsyncSession = Depends(get_session)):
    yield SQLAlchemyUserDatabase(session, User)


async def get_access_token_db(session: AsyncSession = Depends(get_session)):
    yield SQLAlchemyAccessTokenDatabase(session, AccessToken)
