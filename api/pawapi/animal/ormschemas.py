from .schemas import AnimalRead
from ..walk.schemas import WalkRead


class AnimalRelRead(AnimalRead):
    walks: list[WalkRead]
