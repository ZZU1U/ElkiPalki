from flet import *
from ..components.appbar import MyAppBar


async def about_animal(page: Page = None, animal: dict = None, back=None):
    page.clean()
    page.appbar = MyAppBar(title=animal['name'], back=back, bgcolor='#00000000')
    page.add(Image(src=animal['image']))
    page.update()
