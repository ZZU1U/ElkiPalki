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
)
from .pages.animals import AnimalsView


load_dotenv(find_dotenv())


class App:
    async def auth(self, page):
        page.appbar = None
        provider = GoogleOAuthProvider(client_id=os.environ.get('client_id'),
                                       client_secret=os.environ.get('secret'),
                                       redirect_url=os.environ.get('redirect_url'), )

        async def login_click(e):
            await page.login(provider)

        async def guest_click(e):
            await page.client_storage.set_async('access_token', 'guest')
            await page.client_storage.set_async('user_id', '0')
            await self.init(page)
            await page.update_async()

        async def on_login(e):
            await page.client_storage.set_async('access_token', page.auth.token.access_token)
            await page.client_storage.set_async('user_id', page.auth.token.access_token)

        page.on_login = on_login

        await page.add_async(
            Column(
                controls=[
                    Container(height=60),
                    Image(src='logo.png', width=120),
                    Text('Добро пожаловать!', size=24),
                    Container(height=float('inf')),
                    Column(
                        controls=[
                            ElevatedButton("Login with Google", on_click=login_click),
                            ElevatedButton("Continue as guest", on_click=guest_click)
                        ]
                    )
                ],
                auto_scroll=False,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                width=float('inf'),
                spacing=30,
            )
        )

    async def logout(self, e):
        await self.page.client_storage.clear_async()
        await self.page.client_storage.remove('access_token')
        await self.init(self.page)
        await self.page.update_async()

    async def init(self, page: Page):
        page.title = 'Добрые руки'
        page.window_width = 400
        page.window_height = 800
        page.theme_mode = 'light'
        page.scroll = ft.ScrollMode.AUTO

        if page.client_storage.get('access_token'):
            print('LOGED')
            page.appbar = AppBar(
                leading=IconButton(icon=ft.icons.ARROW_BACK, icon_size=20),
                leading_width=40,
                title=ft.Text("Наши животные"),
                actions=[
                    IconButton(icon=ft.icons.LOGOUT, icon_size=20, on_click=self.logout),
                    IconButton(icon=ft.icons.SEARCH, icon_size=20),
                ]
            )
            await page.add_async(
                await AnimalsView(),
            )
        else:
            print('UNLOGED')
            await self.auth(page)

    def __init__(self, page: Page):
        asyncio.run(self.init(page))

        self.page = page

