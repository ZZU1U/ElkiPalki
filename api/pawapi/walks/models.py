from datetime import datetime
from sqlalchemy import ForeignKey, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from pawapi.db.database import Base
from pawapi.db.annotations import intpk


class Walk(Base):
    __tablename__ = "walk"
    id: Mapped[intpk]
    date: Mapped[datetime] = mapped_column(DateTime(timezone=True))
    duration: Mapped[int]
    animal_id: Mapped[int] = mapped_column(ForeignKey("animal.id"))
    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"))
    animal: Mapped["Animal"] = relationship(back_populates='walks', lazy='select')
    user: Mapped["User"] = relationship(back_populates='walks', lazy='select')
