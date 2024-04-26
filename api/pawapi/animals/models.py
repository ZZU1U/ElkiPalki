from datetime import datetime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from pawapi.models import CRUD, Base, intpk
from .enums import AnimalStatus



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
    walks: Mapped[list["Walk"]] = relationship()
