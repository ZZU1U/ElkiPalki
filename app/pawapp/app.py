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
from pawapp.services.settings import write_settings, get_settings
from pawapp.services.admin import AdminService


load_dotenv(find_dotenv())


class App:
    async def close_dialog(self, e):
        self.page.dialog.open = False
        self.page.update()


    async def auth(self, page):
        page.appbar = None
        provider = GoogleOAuthProvider(client_id=os.environ.get('client_id'),
                                       client_secret=os.environ.get('secret'),
                                       redirect_url=os.environ.get('redirect_url'), )

        async def login_click(e):
            await page.login(provider)

        async def guest_click(e):
            write_settings('guest', 0)
            await self.init(page)
            await page.update_async()

        async def admin_login(e):
            if await AdminService.is_admin(self.admin_name.value):
                write_settings('admin', -1)
                await self.close_dialog(None)
                await self.init(self.page)
            else:
                self.admin_error.value = 'You are not admin'
                self.admin_error.visible = True
            await page.update_async()

        async def admin_click(e):
            self.admin_name = TextField('', width=200)
            self.admin_error = Text(visible=False)
            self.page.dialog = AlertDialog(
                title=Text('Введите имя админа'),
                content=Column([Row([
                    self.admin_name,
                    IconButton(icon=ft.icons.SEND, on_click=admin_login),
                ], tight=True), self.admin_error], tight=True),
                modal=True,
                actions=[
                    ft.FilledButton(text='Cancel', on_click=self.close_dialog),
                ]
            )
            self.page.dialog.open = True
            self.page.update()

        async def on_login(e):
            write_settings(page.auth.access_token, page.auth.user.id)
            await self.init(page)
            await page.update_async()

        page.on_login = on_login

        await page.add_async(
            Container(
                content=Column(
                    controls=[
                        Image(src='logo.png', width=120),
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
                height=float('inf'),
            )
        )

    async def logout(self, e):
        write_settings(None, None)
        await self.init(self.page)
        await self.page.update_async()

    async def init(self, page: Page):
        page.clean()
        page.title = 'Добрые руки'
        page.theme_mode = 'light'

        settings = get_settings()
        print(settings)

        if settings['token'] is None:
            await self.auth(page)
        else:
            page.appbar = AppBar(
                leading=IconButton(icon=ft.icons.ARROW_BACK, icon_size=20),
                leading_width=40,
                title=ft.Text("Добрые руки"),
                actions=[
                    IconButton(icon=ft.icons.LOGOUT, icon_size=20, on_click=self.logout),
                    IconButton(icon=ft.icons.SEARCH, icon_size=20),
                ]
            )
            if settings['id'] == -1:
                await page.add_async(
                    Text('ADMIN')
                )
            else:
                await page.add_async(
                    await AnimalsView(),
                )

    def __init__(self, page: Page):
        asyncio.run(self.init(page))
        page.scroll = ft.ScrollMode.AUTO

        self.page = page
        page.window_width = 400
        page.window_height = 800
        page.update()

