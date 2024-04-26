import asyncio
import flet as ft
import os
from flet.auth.providers import GoogleOAuthProvider
from flet import (
    Page,
    Text,
)


class App:
    async def init(self, page):
        provider = GoogleOAuthProvider(client_id=os.getenv("GOOGLE_CLIENT_ID"),
                                       client_secret=os.getenv("GOOGLE_CLIENT_SECRET"),
                                       redirect_url="http://localhost:8550/api/oauth/redirect", )

        def login_click(e):
            page.login(provider)

        def on_login(e):
            print("Access token:", page.auth.token.access_token)
            print("User ID:", page.auth.user.id)

        page.on_login = on_login
        await page.add_async(Text('Привет, собаки!'), ft.ElevatedButton("Login with Google", on_click=login_click))

    def __init__(self, page: Page):

        self.page = Page
        self.cont = ft.Container()

        asyncio.run(self.init(page))

