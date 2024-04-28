import asyncio
from flet import *
from ..components.appbar import MyAppBar
from ..services.admin import AdminService


async def edit_animal(page: Page = None, animal: dict = None, back=None):
    page.clean()
    page.appbar = MyAppBar(title=animal['name'], back=back, bgcolor='#00000000')

    def clicked_submit(e):
        if dd.value == 'Рад встрече с человеком':
            animal["status"] = 'AVAILABLE'
        elif dd.value == 'Нашел дом':
            animal["status"] = 'ADOPTED'
        elif dd.value == 'На передержке':
            animal["status"] = 'OVEREXPOSED'
        else:
            animal["status"] = 'UNAVAILABLE'
        animal['name'] = name.value
        animal['species'] = spicies.value
        animal['food_daily'] = food_daily.value
        animal['image'] = image.value
        animal['age'] = age.value
        animal['description'] = description.value
        asyncio.run(AdminService.change_animal(animal))

    dd = Dropdown(f'{animal["status"]}',
                     width=400,
                     options=[
                         dropdown.Option("Рад встрече с человеком"),
                         dropdown.Option("Нашел дом"),
                         dropdown.Option("На передержке"),
                         dropdown.Option('Не хочет общаться')
                     ],
                  label='статус'
            )
    name = TextField(f'{animal["name"]}', label='имя')
    spicies = TextField(f'{animal["species"]}', label='Вид/порода')
    age = TextField(f'{animal["age"]}', label='Возраст')
    description = TextField(f'{animal["description"]}', multiline=True, label='Описание')
    food_daily = TextField(f'{animal["food_daily"]}', label='Дневная норма')
    image = TextField(f'{animal["image"]}', label='Ссылка на фото')
    page.add(Container(Column(
        controls=[
            Image(
                src=animal['image'],
                width=float('inf'),
                height=400,
                fit=ImageFit.COVER,
            ),
            dd,
            name,
            spicies,
            age,
            description,
            food_daily,
            image,
            FilledButton('Подтвердить', on_click=clicked_submit)
        ]
    ), width=float('inf'), margin=15))
    page.update()
