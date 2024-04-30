from ..animal.schemas import AnimalRead
from pawapi.user.schemas import UserRead
from .schemas import WalkRead


class WalkRelRead(WalkRead):
    user: UserRead
    animal: AnimalRead
