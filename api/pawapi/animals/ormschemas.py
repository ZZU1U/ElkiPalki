from .schemas import AnimalRead
from ..walks.schemas import WalkRead


class AnimalRelRead(AnimalRead):
    walks: list[WalkRead]
