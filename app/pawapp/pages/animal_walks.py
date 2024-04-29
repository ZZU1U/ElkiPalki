from typing import Callable
import flet as ft
import datetime as dt
from datetime import datetime
from ..components.appbar import MyAppBar
from ..services.walk import WalkService
from ..services.user import UserService
import asyncio


async def tablepage(page, animal, back=None):
    rows = []
    page.clean()
    person = UserService.current()
    animal['walks'] = (await WalkService.get_walks_for_animal(animal['id'])).json()
    for i in range(len(animal['walks'])):
        a = datetime.fromisoformat(animal['walks'][i]['date'])
        rows.append(ft.DataRow(cells=[ft.DataCell(ft.Text(datetime.strftime(a, '%d.%m %H:%M'))),
                                           ft.DataCell(ft.Text(animal['walks'][i]['duration'])),
                                                       ft.DataCell(ft.Text(animal['walks'][i]['user']['name'])),]))
    bar = MyAppBar(title='Расписание', back=back)
    def choose_time(e):
        try:
            b = dat.value.split(' ')
            d = b[0].split('.')
            t = b[1].split(':')
            c = dt.datetime(year=2024, day=int(d[0]), month=int(d[1]), hour=int(t[0]), minute=int(t[1]), second=0, microsecond=0)
        except:
            okno.content.controls[0].value=''
            okno.content.controls[0].hint_text='Неправильный формаыт'
            page.update()
            return

        asyncio.run(WalkService.add({
            'user_name': get_settings()['name'],
            'animal_id': animal['id'],
            'date': c.isoformat(),
            'duration': int(tim.value)
        }))
        asyncio.run(tablepage(page, animal, back))

    table = ft.DataTable(columns=[
                ft.DataColumn(ft.Text("Дата")),
                ft.DataColumn(ft.Text("Время")),
                ft.DataColumn(ft.Text("Имя"), numeric=True),
            ],
            rows=rows,
            border=ft.border.all(color='black'),
    heading_row_color='#B9B9B9', vertical_lines=ft.border.BorderSide(1, 'black'), horizontal_lines=ft.border.BorderSide(1, 'black'))
    dat = ft.TextField(label='Дата м.д ч:м', bgcolor='white', width=328, height=47, border_radius=30)
    tim = ft.TextField(label='Продолжительность (мин)', bgcolor='white', width=328, height=47, border_radius=30)
    okno = ft.Container(width=379, height=195, bgcolor='#C27E17',border_radius=30, content=ft.Column(
        controls=[dat,
                  tim,
                  ft.FilledButton('Выбрать время', style=ft.ButtonStyle(bgcolor='#FAD200', color='Black'),
                                  on_click=choose_time)], alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.CENTER
    ))
    page.add(bar, ft.Container(ft.Column(controls=[table, okno], horizontal_alignment=ft.CrossAxisAlignment.CENTER, alignment=ft.MainAxisAlignment.CENTER), width=10000))
