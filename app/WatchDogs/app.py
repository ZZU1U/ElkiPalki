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
        head = ft.Row(controls=[ft.Container(content=ft.Image(src=f'/home/nikola/PycharmProjects/ElkiPalki/app/WatchDogs/image 1.png', width=50, height=48.9)),
                             ft.Container(content=Text('Привет, собаки!', font_family='Caveat'))], alignment=ft.MainAxisAlignment.CENTER)
        sign = ft.Row(controls=[ft.FilledButton("Login with Google", on_click=login_click,
                                               style=buttonstyle)], alignment=ft.MainAxisAlignment.CENTER, vertical_alignment=ft.CrossAxisAlignment.CENTER)
        await page.add_async(ft.Column(controls=[ft.Container(head, height=300), ft.Container(sign)]))

    def __init__(self, page: Page):
        self.page = Page
        self.cont = ft.Container()
        page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
        asyncio.run(self.init(page))

