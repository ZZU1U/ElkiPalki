import asyncio
import flet as ft
import os
from flet.auth.providers import GoogleOAuthProvider
from dotenv import load_dotenv, find_dotenv
from flet import (
    Page,
    Text,
)

load_dotenv(find_dotenv())


class App:
    async def init(self, page: Page):
        provider = GoogleOAuthProvider(client_id=os.environ.get('client_id'),
                                       client_secret=os.environ.get('secret'),
                                       redirect_url=os.environ.get('redirect_url'), )

        def login_click(e):
            page.login(provider)

        def on_login(e):
            page.client_storage.set('access_token', page.auth.token.access_token)
            print("Access token:", page.auth.token.access_token)
            print("User ID:", page.auth.user.id)

        page.on_login = on_login
        await page.add_async(Text('Привет, собаки!'), ft.ElevatedButton("Login with Google", on_click=login_click))

    def __init__(self, page: Page):
        asyncio.run(self.init(page))

        self.page = Page

