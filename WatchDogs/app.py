import asyncio
import flet as ft
from flet import (
    Page,
    Text,
)


class App:
    async def init(self, page):
        await page.add_async(Text('Привет, собаки!'))

    def __init__(self, page: Page):
        asyncio.run(self.init(page))
