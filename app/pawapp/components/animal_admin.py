import flet as ft
import asyncio
from ..pages.edit_animal import edit_animal
from flet import (
    Container,
    Text,
    Image,
    Row,
    Stack,
    LinearGradient,
    Alignment,
    Page
)


class AnimalAdmin(Container):
    def __init__(self, data: 'AnimalRead', *args, **kwargs):
        super().__init__(
            #image_fit=ft.ImageFit.FIT_WIDTH,
            #image_src=data['image'],
            height=100,
            expand=False,
            alignment=ft.alignment.bottom_left,
            content=Container(

                    ft.Stack([Text(
                        f'{data["name"]}, {data["age"]}, {data["species"]}',
                        size=30,
                        color='black',
                        text_align=ft.alignment.bottom_left,
                    )], alignment=ft.alignment.center)
                ,
            ),
            on_click=lambda e: asyncio.run(edit_animal(animal=data, **kwargs)),
            border_radius=30,
            margin=10,
        )
