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

buttonstyle = ft.ButtonStyle(bgcolor=ft.colors.BLUE_900)
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
        cont = ft.Container(ft.Row(controls=[ft.Image(src=f'/home/nikola/PycharmProjects/ElkiPalki/app/WatchDogs/image 1.png', width=50,
        height=48.9,
        fit=ft.ImageFit.CONTAIN), Text('Привет, собаки!', font_family='Caveat')]))
        await page.add_async(ft.Column(controls=[cont,
                             ft.FilledButton("Login with Google", on_click=login_click,
                                               style=buttonstyle)]))

    def __init__(self, page: Page):

        self.page = Page

        self.cont = ft.Container()
        page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        asyncio.run(self.init(page))

