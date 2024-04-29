from enum import Enum


class AnimalStatus(Enum):
    available = 'AVAILABLE'
    adopted = 'ADOPTED'
    overexposed = 'OVEREXPOSED'
    unavailable = 'UNAVAILABLE'

