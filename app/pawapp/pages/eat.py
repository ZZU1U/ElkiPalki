from flet import *
from pawapp import styles
from ..components.appbar import MyAppBar
from ..pages.animal_walks import tablepage
import asyncio

async def donate_eat(page, animal, back):
    page.clean()
    def thanksfordonate(e):
        dlg = AlertDialog(content=Text('Спасибо за пожертвование'), open=True)
        page.dialog = dlg
        page.update()

    bar = MyAppBar(title='Корма', back=back)
    bar.center_title = True
    btn = FilledButton('Пожертвовать', width=211, height=45, on_click=thanksfordonate,
                       style=ButtonStyle(bgcolor='#FA7800'))
    t = Text('Адрес приюта: Приют “Верный”, ул. 40 лет Октября, 2/16')
    c = Container(content=Column(controls=[btn, t],
                                 horizontal_alignment=CrossAxisAlignment.CENTER,
                                 alignment=MainAxisAlignment.CENTER),
                  width=float('inf'), height=600)
    page.add(bar, c)