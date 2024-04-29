
from pawapi.db.database import engine
from pawapi.router import app


admin = Admin(app, engine)


admin.add_view(UserAdmin)
admin.add_view(AnimalAdmin)
admin.add_view(WalkAdmin)
