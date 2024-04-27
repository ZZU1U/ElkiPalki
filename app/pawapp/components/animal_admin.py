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
            image_fit=ft.ImageFit.FIT_WIDTH,
            image_src=data['image'],
            height=250,
            expand=False,
            alignment=ft.alignment.bottom_left,
            content=Stack(
                [
                    Container(gradient=LinearGradient(
                        begin=ft.alignment.top_center,
                        end=ft.alignment.bottom_center,
                        colors=[
                            '#00000000',
                            '#FF000000',
                        ]
                    )),
                    Text(
                        f'{data["name"]}, {data["age"]}',
                        size=30,
                        color='#FFFFFF',
                        text_align=ft.alignment.bottom_left,
                        left=10,
                        bottom=10,
                    )
                ],
            ),
            on_click=lambda e: asyncio.run(edit_animal(animal=data, **kwargs)),
            border_radius=30,
            margin=10,
        )
