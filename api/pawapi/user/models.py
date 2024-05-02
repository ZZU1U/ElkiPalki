from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy_utils.types import PhoneNumber, PhoneNumberType, Password, PasswordType
from sqlalchemy_utils import force_auto_coercion

from ..db.database import Base
from ..db.annotations import intpk

force_auto_coercion()


class User(Base):
    __tablename__ = "user"
    id: Mapped[intpk]
    name: Mapped[str]
    password: Mapped[Password] = mapped_column(
        PasswordType(
            schemes=[
                'pbkdf2_sha512',
                'md5_crypt'
            ],
            deprecated=['md5_crypt'],
            max_length=100
        )
    )
    phone: Mapped[PhoneNumber] = mapped_column(
        PhoneNumberType(
            region='RU'
        ),
        unique=True
    )
    is_volunteer: Mapped[bool] = mapped_column(default=False)
    is_superuser: Mapped[bool] = mapped_column(default=False)
    walks: Mapped[list["Walk"]] = relationship(
        lazy='selectin',
        back_populates='user'
    )

    def __repr__(self):
        return f"<User(id={self.id}, phone={self.phone}, pwd={self.password})>"
