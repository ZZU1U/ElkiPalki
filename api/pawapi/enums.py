from enum import Enum


class Role(Enum):
    user = 'USER'
    volunteer = 'VOLUNTEER'
    admin = 'ADMIN'


class AnimalStatus(Enum):
    available = 'AVAILABLE'
    adopted = 'ADOPTED'
    overexposed = 'OVEREXPOSED'
    unavailable = 'UNAVAILABLE'

