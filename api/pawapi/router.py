from fastapi import FastAPI
from .animals.router import router as animals_router

app = FastAPI(title="Paw API")
app.include_router(animals_router)
