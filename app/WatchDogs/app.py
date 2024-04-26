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
api_keys = 'AIzaSyCC0s7_MNGY-3Lq2VfH6jXzB748TF9LByQ'

class App:
    async def init(self, page):
        provider = GoogleOAuthProvider(client_id=os.environ.get('client_id'),
                                       client_secret=os.environ.get('secret'),
                                       redirect_url=os.environ.get('redirect_url'), )

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

