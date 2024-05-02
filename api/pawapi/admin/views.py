from sqladmin import ModelView
from fastapi import Request

from pawapi.walk.models import Walk
from pawapi.user.models import User
from pawapi.animal.models import Animal
from .auth import authentication_backend


class Permissions:
    async def is_visible(self, request: Request) -> bool:
        return await authentication_backend.authenticate(request)

    async def is_accessible(self, request: Request) -> bool:
        return await authentication_backend.authenticate(request)


class UserAdmin(Permissions, ModelView, model=User):

    name = "Users"
    name_plural = "Users"
    icon = "fa-solid fa-user"

    column_list = [User.id, User.name, User.phone]

    can_edit = False
    can_delete = False


class AnimalAdmin(Permissions, ModelView, model=Animal):
    name = "Animals"
    name_plural = "Animals"
    icon = "fa-solid fa-dog"

    column_list = [Animal.id, Animal.status, Animal.species, Animal.name, Animal.age, Animal.description]


class WalkAdmin(Permissions, ModelView, model=Walk):
    name = "Walks"
    name_plural = "Walks"
    icon = "fa-solid fa-person-walking"

    column_list = [Walk.id, Walk.date, Walk.duration, Walk.user, Walk.animal]
