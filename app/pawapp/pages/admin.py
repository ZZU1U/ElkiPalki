from flet import Text, Page
import flet as ft
import asyncio
from ..components.appbar import MyAppBar
from ..pages.adminchoices import adminchoice

async def AdminPage(page: Page, back=None):
    def runchoice(e):
        asyncio.run(adminchoice(page, lambda e: asyncio.run(AdminPage(page, back))))
        page.update()
    page.clean()
    page.appbar = MyAppBar(title='Панель админа', back=back)
    page.appbar.center_title = True
    btn1 = ft.FilledButton(text='Список прогулок',
                           width=220,
                           height=45,
                           style=ft.ButtonStyle(bgcolor='#FA7800'))
    btn2 = ft.FilledButton(text='Корма',
                           width=220,
                           height=45,
                           style=ft.ButtonStyle(bgcolor='#FA7800'))
    btn3 = ft.FilledButton(text='Добавить животное',
                           width=220,
                           height=45,
                           style=ft.ButtonStyle(bgcolor='#FA7800'), on_click=runchoice)

    page.auto_scroll = False
    page.add(ft.Container(ft.Column(controls=[btn1, btn2, btn3], alignment=ft.MainAxisAlignment.CENTER,
                                   horizontal_alignment=ft.CrossAxisAlignment.CENTER), width=float('inf'), height=600))
