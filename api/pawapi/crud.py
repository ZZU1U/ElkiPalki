from sqlalchemy import select
from .database import session_factory


class CRUD:
    id: int
    def __init__(self, *args, **kwargs):
        pass

    def __repr__(self):
        return f'<{self.__class__.__name__} {self.id}>'

    @staticmethod
    async def add(model):
        async with session_factory() as session:
            session.add(model)
            await session.commit()

    @classmethod
    async def all(cls):
        async with session_factory() as session:
            return (await session.execute(select(cls))).unique().scalars().all()

    @classmethod
    async def change(cls, obj):
        async with session_factory() as session:
            stmt = select(cls).where(cls.id == obj.id)
            old_obj = await session.execute(stmt)
            print(old_obj.unique().scalar())
            return old_obj.unique().scalar()
