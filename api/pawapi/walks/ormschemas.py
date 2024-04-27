from ..animals.schemas import AnimalRead
from ..users.schemas import UserRead
from .schemas import WalkRead, WalkWrite


class WalkRelRead(WalkRead):
    user: UserRead
    animal: AnimalRead
