from typing import Annotated
from sqlalchemy.orm import Mapped, mapped_column, relationship
from .database import Base
from .crud import CRUD
from .enums import Role


intpk = Annotated[int, mapped_column(primary_key=True)]


class User(Base, CRUD):
    __tablename__ = "user"
    id: Mapped[intpk]
    name: Mapped[str]
    role: Mapped[Role] = mapped_column()
    walks: Mapped[list["Walk"]] = relationship()
