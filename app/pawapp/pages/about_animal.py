from flet import *
from ..components.appbar import MyAppBar


async def about_animal(page: Page = None, animal: dict = None, back=None):
    page.clean()
    page.appbar = MyAppBar(title=animal['name'], back=back, bgcolor='#00000000')
    page.add(Column(
        controls=[
            Image(
                src=animal['image'],
                width=float('inf'),
                height=400,
                fit=ImageFit.COVER,
            ),
            Text(f'{animal["status"]}'),
            Text(f'{animal["food_donated"]} ({int(animal["food_donated"] / animal["food_daily"])} дней)')
        ]
    ))
    page.update()
