import flet as ft
from flet import (
    Container,
    Text,
    Image,
    Row,
    Stack,
    LinearGradient,
    Alignment
)


class Animal(Container):
    def __init__(self, data: 'AnimalRead', *args, **kwargs):
        super().__init__(
            *args,
            **kwargs,
            image_fit=ft.ImageFit.FIT_WIDTH,
            image_src=data['image'],
            height=250,
            expand=False,
            alignment=ft.alignment.bottom_left,
            content=Stack(
                [
                    Text(
                        f'{data["name"]}, {data["age"]}',
                        size=30,
                        color='#FFFFFF',
                        text_align=ft.alignment.bottom_left,
                        bgcolor='blue'
                    ),
                    Container(gradient=LinearGradient(
                        begin=ft.alignment.top_center,
                        end=ft.alignment.bottom_center,
                        colors=[
                            '#00000000',
                            '#FF000000',
                        ]
                    )),
                ],
            ),
            border_radius=30,
            bgcolor='gray',
        )
