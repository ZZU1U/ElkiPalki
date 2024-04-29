from flet import (
    Page,
    Container,
    Column,
    Image,
    Text,
    ElevatedButton,
    MainAxisAlignment,
    CrossAxisAlignment,
    margin
)


from ..components.login_form import LoginForm
from ..components.register_form import RegisterForm


def welcome(page: Page):
    page.add(
        Container(
            content=Column(
                controls=[
                    Image(src='logo.png', width=160),
                    Text('Добро пожаловать!', size=24),
                    Container(
                        content=Column(
                            controls=[
                                ElevatedButton(
                                    "Вход",
                                    on_click=lambda _: LoginForm(
                                        page,
                                        back=lambda _: welcome(page)
                                    )
                                ),
                                ElevatedButton("Регистрация", on_click=lambda _: RegisterForm(page)),
                            ],
                            alignment=MainAxisAlignment.END,
                            horizontal_alignment=CrossAxisAlignment.CENTER,
                        )
                    )
                ],
                horizontal_alignment=CrossAxisAlignment.CENTER,
                spacing=30,
            ),
            width=float('inf'),
            margin=margin.symmetric(60, 0),
        )
    )
    page.update()
