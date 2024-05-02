from sqlalchemy import select
from sqlalchemy_utils import PhoneNumber

from pawapi.db.database import session_factory
from ..models import User
from .manager import manager


@manager.user_loader()
async def load_user(phone: str) -> User | None:
    async with session_factory() as session:
        stmt = (
            select(User)
            .where(User.phone == phone)
        )

        user = await session.scalar(stmt)

        return user
