from .schemas import *
from ..walks.schemas import *
from ..users.schemas import *


class AnimalRelRead(AnimalRead):
    walks: list[WalkRead]
