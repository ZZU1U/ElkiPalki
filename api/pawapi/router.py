from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from .animal.router import router as animals_router
from .user.auth.router import router as auth_router
from .walk.router import router as walks_router
from .cli import create_all


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
