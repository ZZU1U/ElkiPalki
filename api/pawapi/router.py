from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from sqladmin import Admin

from .admin.views import UserAdmin, AnimalAdmin, WalkAdmin
from .animals.router import router as animals_router
from .user.auth.router import router as auth_router
from .walks.router import router as walks_router
from .cli import create_all
from .db.database import engine


app = FastAPI(
    lifespan=create_all,
    title="Paw API",
)

app.include_router(animals_router)
app.include_router(walks_router)
app.include_router(auth_router)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
)

admin = Admin(app, engine)

admin.add_view(UserAdmin)
admin.add_view(AnimalAdmin)
admin.add_view(WalkAdmin)
