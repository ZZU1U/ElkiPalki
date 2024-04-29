from ..animals.schemas import AnimalRead
from pawapi.auth.schemas import UserRead
from .schemas import WalkRead


class WalkRelRead(WalkRead):
    user: UserRead
    animal: AnimalRead
