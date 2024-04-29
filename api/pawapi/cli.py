import typer
from contextlib import asynccontextmanager
from pawapi.db.database import create_tables
from pawapi.db.test import test

cli = typer.Typer()


@asynccontextmanager
@cli.command()
async def create_all(app=None):
    await create_tables()
    await test()
    yield


@cli.command()
async def refresh_tables():
    await create_tables()


if __name__ == "__main__":
    cli()
