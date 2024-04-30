from sqlalchemy.orm import Mapped, mapped_column, relationship

from ..db.database import Base
from ..db.annotations import intpk


class User(Base):
    __tablename__ = "user"
    id: Mapped[intpk]
    name: Mapped[str]
    hashed_password: Mapped[str]
    phone: Mapped[str] = mapped_column(unique=True)
    is_volunteer: Mapped[bool] = mapped_column(default=False)
    is_superuser: Mapped[bool] = mapped_column(default=False)
    walks: Mapped[list["Walk"]] = relationship(lazy='selectin', back_populates='user')
