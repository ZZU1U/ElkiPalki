import flet as ft
from ..components.appbar import MyAppBar
from ..components.animal_admin import AnimalAdmin
from ..services.animals import AnimalService
import asyncio



async def adminchoice(page: ft.Page, back=None):
    page.clean()
    animals = (await AnimalService.get_animals()).json()
    page.appbar = MyAppBar(title='Панель админа', back=back)
    page.appbar.center_title = True
    lv = ft.ListView()
    for i in range(len(animals)):
        lv.controls.append(
            AnimalAdmin(animals[i], page=page, back=(lambda e: asyncio.run(adminchoice(page, back)))))

    page.add(lv)
