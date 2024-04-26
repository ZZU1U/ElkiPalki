from datetime import datetime
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from pawapi.models import CRUD, Base, intpk

class Walk(Base, CRUD):
    __tablename__ = "walk"
    id: Mapped[intpk]
    date: Mapped[datetime]
    duration: Mapped[int]
    animal_id: Mapped[int] = mapped_column(ForeignKey("animal.id"))
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    animal: Mapped["Animal"] = relationship(back_populates='walks')
    user: Mapped["User"] = relationship(back_populates='walks')
