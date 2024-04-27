from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .animals.router import router as animals_router
from .users.router import router as users_router
from .walks.router import router as walks_router
from .database import create_tables
from .test import test


@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_tables()
    await test()
    yield

app = FastAPI(
    lifespan=lifespan,
    title="Paw API",
)
app.include_router(animals_router)
app.include_router(users_router)
app.include_router(walks_router)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
