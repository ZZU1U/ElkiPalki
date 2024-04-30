from sqladmin import Admin
from ..db.database import engine, session_factory
from ..router import app
from .views import UserAdmin, AnimalAdmin, WalkAdmin
from .auth import authentication_backend


admin = Admin(
    app=app,
    engine=engine,
    session_maker=session_factory,
    authentication_backend=authentication_backend
)

admin.add_view(UserAdmin)
admin.add_view(AnimalAdmin)
admin.add_view(WalkAdmin)
