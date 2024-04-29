from flet import (
    AlertDialog,
    Text,
    Column,
    FilledButton,
    Page,
    ControlEvent,
    TextField
)

from ..services.user import UserService


class RegisterForm(AlertDialog):
    """
    This class represents the registration form.
    While initializing it also shows itself.
    """
    def __init__(self, page: Page):
        def submit(e: ControlEvent):
            if not name.value:
                name.error_text = 'Вы забыли ввести имя'

            response = UserService.register(
                name.value,
                email.value,
                pwd.value,
                phone.value
            )
            print(response)
            page.close_dialog()


        name = TextField(label='Имя')
        pwd = TextField(label='Пароль', password=True, can_reveal_password=True)
        email = TextField(label='Пощта')
        phone = TextField(label='Телефон')

        super().__init__(
            title=Text('Регистрация'),
            content=Column(
                controls=[
                    name,
                    email,
                    phone,
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
