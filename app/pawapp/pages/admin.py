from flet import Text, Page
import flet as ft
from ..components.appbar import MyAppBar


async def AdminPage(page: Page, back=None):
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
                           style=ft.ButtonStyle(bgcolor='#FA7800'))
    page.auto_scroll = False
    page.add(ft.Container(ft.Column(controls=[btn1, btn2, btn3], alignment=ft.MainAxisAlignment.CENTER,
                                   horizontal_alignment=ft.CrossAxisAlignment.CENTER), width=float('inf'), height=600))
