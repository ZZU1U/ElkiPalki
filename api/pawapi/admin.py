from sqladmin import Admin, ModelView

from .walks.models import Walk
from pawapi.user.models import User
from .animals.models import Animal
from .db.database import engine
from .router import app


admin = Admin(app, engine)


class UserAdmin(ModelView, model=User):
    name = "Users"
    name_plural = "Users"
    icon = "fa-solid fa-user"

    column_list = [User.id, User.name, User.phone, User.email]

    can_edit = False
    can_delete = False


class AnimalAdmin(ModelView, model=Animal):
    name = "Animals"
    name_plural = "Animals"
    icon = "fa-solid fa-dog"

    column_list = [Animal.id, Animal.status, Animal.species, Animal.name, Animal.age, Animal.description]


class WalkAdmin(ModelView, model=Walk):
    name = "Walks"
    name_plural = "Walks"
    icon = "fa-solid fa-person-walking"

    column_list = [Walk.id, Walk.date, Walk.duration, Walk.user, Walk.animal]


admin.add_view(UserAdmin)
admin.add_view(AnimalAdmin)
admin.add_view(WalkAdmin)
