from flet import *
from pawapp import styles
from ..components.appbar import MyAppBar
from ..pages.animal_walks import tablepage
import asyncio

STATUSES = {
    'AVAILABLE': 'Рад встрече с человеком',
    'ADOPTED': 'Нашел дом',
    'OVEREXPOSED': 'На передержке',
    'UNAVAILABLE': 'Не хочет общаться'
}


async def about_animal(page: Page = None, animal: dict = None, back=None):
    page.clean()
    page.appbar = MyAppBar(title=f'{animal["name"]}, {animal["species"]}', back=back, bgcolor='#00000000')
    page.add(Column(
        controls=[
            Image(
                src=animal['image'],
                width=float('inf'),
                height=300,
                fit=ImageFit.COVER,
            ),
            Container(
                Column(controls=[
                    Text(animal['description']),
                    Text(f'Статус: {STATUSES.get(animal["status"])}'),
                    Text(f'Получил корма: {animal["food_donated"]} ({int(animal["food_donated"] / animal["food_daily"])} дней)'),
                ], width=float('inf')),
                margin=margin.symmetric(0, 10)
            ),
            Container(height=100),
            Column(controls=[
                FilledButton('Взять опекунство', width=200, style=styles.button_style,),
                FilledButton('Помочь кормом', width=200, style=styles.button_style),
                FilledButton('Прогуляться за лапку', width=200, style=styles.button_style, on_click=lambda e: asyncio.run(tablepage(page, about_animal))),
            ], spacing=20, horizontal_alignment=CrossAxisAlignment.CENTER, width=float('inf')),
        ],
    ))
    page.update()
