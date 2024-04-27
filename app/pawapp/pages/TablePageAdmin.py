import flet as ft
import datetime as dt
from datetime import datetime
from ..components.appbar import MyAppBar
from ..services.animals import AnimalService
from ..services.walks import WalksService


async def tablepageadmin(page, back=None):
    rows = []
    page.clean()
    all_walks = (await WalksService.get_all()).json()
    print(all_walks)
    animals = (await AnimalService.get_animals()).json()
    for i in range(len(all_walks)):
        a = datetime.strptime(all_walks[i]['date'], '%Y-%m-%dT%H:%M:%S.%f')
        rows.append(ft.DataRow(cells=[ft.DataCell(ft.Text(datetime.strftime(a, '%d.%m %H:%M'))),
                                           ft.DataCell(ft.Text(all_walks[i]['duration'])),
                                                       ft.DataCell(ft.Text(all_walks[i]['user']['name'])),
                                                                   ft.DataCell(ft.Checkbox())]))
    bar = MyAppBar(title='Расписание', back=back)
    table = ft.DataTable(columns=[
                ft.DataColumn(ft.Text("Дата")),
                ft.DataColumn(ft.Text("Время")),
                ft.DataColumn(ft.Text("Имя")),
                ft.DataColumn(ft.Text('Выбор'), numeric=True)
            ],
            rows=rows,
            border=ft.border.all(color='black'),
    heading_row_color='#B9B9B9', vertical_lines=ft.border.BorderSide(1, 'black'), horizontal_lines=ft.border.BorderSide(1, 'black'))
    btn = ft.FilledButton('Удалить', width=211, height=45, style=ft.ButtonStyle(bgcolor='#FA7800'))
    page.add(bar, ft.Container(ft.Column(controls=[table, btn], horizontal_alignment=ft.CrossAxisAlignment.CENTER, alignment=ft.MainAxisAlignment.CENTER), width=10000))



