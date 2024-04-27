import asyncio
import flet as ft
import re
import os
from flet.auth.providers import GoogleOAuthProvider
from dotenv import load_dotenv, find_dotenv
from flet import (
    Page,
    Text,
    AppBar,
    IconButton,
    Icon,
    Column,
    Image,
    Container,
    ElevatedButton,
    AlertDialog,
    Row,
    TextField
)
from .pages.animals import AnimalsView
from .pages.admin import AdminPage
from .services.settings import write_settings, get_settings
from .services.admin import AdminService


load_dotenv(find_dotenv())


class App:
    def auth(self, page):
        page.clean()
        page.appbar = None
        provider = GoogleOAuthProvider(client_id=os.environ.get('client_id'),
                                       client_secret=os.environ.get('secret'),
                                       redirect_url=os.environ.get('redirect_url'), )

        def login_click(e):
            page.login(provider)

        def guest_click(e):
            def cancel(e):
                dlg.open = False
                page.update()
            def user_submit(e):
                result = bool(re.match(
                    r'^(\+7|7|8)?[\s\-]?\(?[489][0-9]{2}\)?[\s\-]?[0-9]{3}[\s\-]?[0-9]{2}[\s\-]?[0-9]{2}$', phone.value))
                print(result)
                if result and name.value != '':
                    dlg.open = False
                    write_settings(role='guest', name=name.value, phone=phone.value)
                    asyncio.run(AnimalsView(page, self.logout))
                else:
                    if not result and name.value == '':
                        phone.value = 'Непрвильный номер'
                        name.value = 'Неправильное имя'
                    elif not result:
                        phone.value = 'Непрвильный номер'
                    else:
                        name.value = 'Неправильное имя'
                page.update()
            name = ft.TextField(label='Введите имя', width=300)
            phone = ft.TextField(label='Введите номер телефона', width=300)
            dlg = ft.AlertDialog(content=ft.Column(controls=[
                name, phone,
                ],
                tight=True
            ), actions=[ft.ElevatedButton('Подтвердить', on_click=user_submit),
                        ft.ElevatedButton('Отмена', on_click=cancel)], open=True)
            page.dialog = dlg
            page.update()

        def admin_login(e):
            if asyncio.run(AdminService.is_admin(self.admin_name.value)):
                write_settings(role='ADMIN')
                page.close_dialog()
                page.update()
                asyncio.run(AdminPage(page, self.logout))
            else:
                self.admin_error.value = 'You are not admin'
                self.admin_error.visible = True
            page.update()

        def admin_click(e):
            self.admin_name = TextField('', width=200)
            self.admin_error = Text(visible=False)
            self.dialog = AlertDialog(
                title=Text('Введите имя админа'),
                content=Column(
                    controls=[
                        Row(
                            controls=[
                                    self.admin_name,
                                    IconButton(
                                        icon=ft.icons.NAVIGATE_NEXT,
                                        on_click=admin_login
                                    ),
                                ],
                            tight=True
                        ),
                        self.admin_error
                    ],
                    tight=True
                ),
                actions=[
                    ft.FilledButton(text='Cancel', on_click=lambda e: page.close_dialog()),
                ]
            )
            self.page.dialog = self.dialog
            self.dialog.open = True
            self.page.update()

        def on_login(e):
            write_settings(access_token=page.auth.access_token, user_id=page.auth.user.id)
            asyncio.run(AnimalsView(page, self.logout))
            page.update()

        page.on_login = on_login

        page.add(
            Container(
                content=Column(
                    controls=[
                        Image(src='logo.png', width=160),
                        Text('Добро пожаловать!', size=24),
                        Container(
                            content=Column(
                                controls=[
                                    ElevatedButton("Login with Google", on_click=login_click),
                                    ElevatedButton("Continue as guest", on_click=guest_click),
                                    ElevatedButton("Admin panel", on_click=admin_click),
                                ],
                                alignment=ft.MainAxisAlignment.END,
                                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                            )
                        )
                    ],
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    width=float('inf'),
                    spacing=30,
                ),
                margin=ft.margin.symmetric(60, 0),
            )
        )

    def logout(self, e):
        write_settings()
        self.auth(self.page)
        self.page.update()

    async def init(self, page: Page):
        page.clean()
        page.title = 'Добрые руки'
        page.theme_mode = 'light'

        settings = get_settings()

        if settings.get('role', None) is None:
            self.auth(page)
        else:
            if settings.get('role') == 'ADMIN':
                await AdminPage(page, back=self.logout)
            else:
                await AnimalsView(page, back=self.logout)

    def __init__(self, page: Page):
        asyncio.run(self.init(page))
        page.scroll = ft.ScrollMode.AUTO
        page.padding = ft.padding.all(0)

        self.page = page
        page.window_width = 400
        page.window_height = 800
        page.update()

