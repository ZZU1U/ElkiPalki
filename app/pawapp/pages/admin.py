from flet import Text, Page
import flet as ft
import asyncio
from ..components.appbar import MyAppBar
from ..pages.adminchoices import adminchoice
from ..pages.table_admin import tablepageadmin

async def AdminPage(page: Page, back=None):

    async def walksadmin(e):
        await tablepageadmin(page, back=lambda e: asyncio.run(AdminPage(page, back)))
    def runchoice(e):
        asyncio.run(adminchoice(page, lambda e: asyncio.run(AdminPage(page, back))))
        page.update()
    page.clean()
    page.appbar = MyAppBar(title='Панель админа', back=back)
    page.appbar.center_title = True
    btn1 = ft.FilledButton(text='Список прогулок',
                           width=220,
                           height=45,
                           style=ft.ButtonStyle(bgcolor='#FA7800'),
                           on_click=walksadmin)

    btn3 = ft.FilledButton(text='Управление',
                           width=220,
                           height=45,
                           style=ft.ButtonStyle(bgcolor='#FA7800'), on_click=runchoice)

    page.auto_scroll = False
    page.add(ft.Container(ft.Column(controls=[btn1, btn3], alignment=ft.MainAxisAlignment.CENTER,
                                   horizontal_alignment=ft.CrossAxisAlignment.CENTER), width=float('inf'), height=600))
