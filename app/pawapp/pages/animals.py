from flet import ListView, Column, Page
from typing import Callable
from ..components.appbar import MyAppBar
from ..components.animal import Animal
from ..services.animal import AnimalService


def animals_view(page: Page, back: Callable = None):
    page.clean()

    page.appbar = MyAppBar('Наши животные', back=back, actions=[])

    animals = AnimalService.read_all()

    page.add(
        ListView(
            list(
                map(
                    lambda animal: Animal(
                        animal,
                        page=page,
                        back=(lambda e: animals_view(page, back))
                    ),
                    animals
                )
            ),
            spacing=10
        )
    )
