import asyncio
import flet as ft
from .registration import registr
from flet import (
    Page,
    Text,
)


class App:
    async def init(self, page):
        await page.add_async(Text('Привет, собаки!'))

    def __init__(self, page: Page):

        self.page = Page
        self.cont = ft.Container(content=registr(self))
        #
        asyncio.run(self.init(page))
