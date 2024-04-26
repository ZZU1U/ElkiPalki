import asyncio
import flet as ft
import os
from flet.auth.providers import GoogleOAuthProvider
from dotenv import load_dotenv, find_dotenv
from flet import (
    Page,
    Text,
)
from .pages.animals import AnimalsView


load_dotenv(find_dotenv())


class App:
    async def _init(self, page: Page):
        provider = GoogleOAuthProvider(client_id=os.environ.get('client_id'),
                                       client_secret=os.environ.get('secret'),
                                       redirect_url=os.environ.get('redirect_url'), )

        def login_click(e):
            page.login(provider)

        def guest_click(e):
            page.client_storage.set('access_token', 'guest')
            page.client_storage.set('user_id', '0')

        def on_login(e):
            print("Access token:", page.auth.token.access_token)
            print("User ID:", page.auth.user.id)
            page.client_storage.set_async('access_token', page.auth.token.access_token)
            page.client_storage.set_async('user_id', page.auth.token.access_token)

        page.on_login = on_login

        if page.client_storage.contains_key('access_token'):
            await page.add_async(
                AnimalsView()
            )
        else:
            await page.add_async(
                Text('Привет, собаки!'),
                ft.ElevatedButton("Login with Google", on_click=login_click),
                ft.ElevatedButton("Continue as guest", on_click=guest_click)
            )

    def __init__(self, page: Page):
        asyncio.run(self._init(page))

        self.page = Page

