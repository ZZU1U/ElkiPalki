import asyncio
from datetime import datetime

from pawapi.db.database import create_tables, session_factory
from pawapi.db.models import User, Animal, Role, Walk


# sudo -i -u postgres
# psql -h localhost -p 5432 -U postgres -d paw

async def test():
    await create_tables()
    me = User(name='Gleb', role=Role.user)
    old_dog = Animal(
        name='Jack',
        age=12,
        description='A nice old dog Jack',
    )
    my_walk = Walk(date=datetime.today(), duration=30, animal=old_dog, user=me)

    await User.add(me)
    await Animal.add(old_dog)
    await Walk.add(my_walk)
    print(await User.all())
    print(await Animal.all())
    print(await Walk.all())


asyncio.run(test())
