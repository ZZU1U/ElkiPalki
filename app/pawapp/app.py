import flet as ft
from flet import (
    Page,
)
from .pages.welcome import welcome
from .pages.animals import animals_view
from .services.settings import Settings
from .services.user import UserService


class App:
    def logout(self, e):
        UserService.logout()
        Settings.clear()
        welcome(self.page)
        self.page.update()

    def __init__(self, page: Page):
        page.title = 'Добрые руки'
        page.theme_mode = 'light'
        page.scroll = ft.ScrollMode.AUTO
        page.padding = ft.padding.all(0)
        Settings.init()

        token = Settings.token()
        if not token:
            welcome(page)
        else:
            animals_view(page)

        page.window_width = 400
        page.window_height = 800
        page.update()
        self.page = page

