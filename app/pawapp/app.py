import asyncio
import flet as ft
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
            write_settings('guest', 0)
            asyncio.run(AnimalsView(page, self.logout))
            page.update()

        def admin_login(e):
            if asyncio.run(AdminService.is_admin(self.admin_name.value)):
                write_settings('admin', -1)
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
            write_settings(page.auth.access_token, page.auth.user.id)
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
        write_settings(None, None)
        self.auth(self.page)
        self.page.update()

    async def init(self, page: Page):
        page.clean()
        page.title = 'Добрые руки'
        page.theme_mode = 'light'

        settings = get_settings()

        if settings['token'] is None:
            self.auth(page)
        else:
            if settings['id'] == -1:
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

