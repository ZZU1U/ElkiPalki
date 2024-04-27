from sqlalchemy import select
from sqlalchemy.orm import joinedload
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
            stmt = select(cls)
            return (await session.execute(stmt)).unique().scalars().all()

    @classmethod
    async def change(cls, obj):
        async with session_factory() as session:
            old_obj = await session.get(cls, obj.id)
            for key, value in obj.__dict__.items():
                setattr(old_obj, key, value)
            await session.commit()
            print(old_obj.__dict__)
            return old_obj
