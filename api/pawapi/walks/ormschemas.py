from ..animals.schemas import AnimalRead
from ..users.schemas import UserRead
from .schemas import WalkRead


class WalkRelRead(WalkRead):
    user: UserRead
    animal: AnimalRead
