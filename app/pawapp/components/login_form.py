from typing import Callable
from flet import (
    AlertDialog,
    Text,
    Column,
    FilledButton,
    Page,
    ControlEvent,
    TextField,
)

from ..services.user import UserService
from ..pages.animals import animals_view


class LoginForm(AlertDialog):
    def __init__(self, page: Page, back: Callable = None):
        def submit(e: ControlEvent):
            response = UserService.login(
                email.value,
                pwd.value,
            )
            animals_view(page, back=back)
            page.close_dialog()

        pwd = TextField(label='Пароль', password=True, can_reveal_password=True)
        email = TextField(label='Пощта')

        super().__init__(
            title=Text('Вход'),
            content=Column(
                controls=[
                    email,
                    pwd
                ],
                tight=True
            ),
            actions=[
                FilledButton(text='Отмена', on_click=lambda e: page.close_dialog()),
                FilledButton(text='Подтвердить', on_click=submit)
            ],
            open=True
        )

        page.dialog = self
        page.update()
