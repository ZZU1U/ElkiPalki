from typing import Callable
import flet as ft
import datetime as dt
animal = {'walks': [
        {'date_start': dt.date(1941, 12, 1), 'duration': 30, 'person_id': 12}
    ]}
def tablepage(page: ft.Page, back: Callable):
    rows = []
    for i in range(len(animal['walks'])):
        rows.append(ft.DataRow(cells=[ft.DataCell(ft.Text(animal['walks'][i]['date_start'])),
                                           ft.DataCell(ft.Text(animal['walks'][i]['duration'])),
                                                       ft.DataCell(ft.Text(animal['walks'][i]['person_id']))]))
    bar = ft.AppBar(leading=ft.IconButton(ft.icons.ARROW_BACK, bgcolor='#FFBB36'),
                    title=ft.Text('Расписание'), bgcolor='Orange',
                    center_title=True
                    )
    table = ft.DataTable(columns=[
                ft.DataColumn(ft.Text("Дата")),
                ft.DataColumn(ft.Text("Время")),
                ft.DataColumn(ft.Text("Имя"), numeric=True),
            ],
            rows=rows,
            border=ft.border.all(color='black'),
    heading_row_color='#B9B9B9', vertical_lines=ft.border.BorderSide(1, 'black'), horizontal_lines=ft.border.BorderSide(1, 'black'))
    okno = ft.Container(width=379, height=195, bgcolor='#C27E17',border_radius=30, content=ft.Column(
        controls=[ft.TextField('date', bgcolor='white', width=328, height=47, border_radius=30),
                  ft.TextField('time', bgcolor='white', width=328, height=47, border_radius=30),
                  ft.FilledButton('choose time', style=ft.ButtonStyle(bgcolor='#FAD200', color='Black'))], alignment=ft.MainAxisAlignment.CENTER, horizontal_alignment=ft.CrossAxisAlignment.CENTER
    ))
    page.add(bar, ft.Container(ft.Column(controls=[table, okno], horizontal_alignment=ft.CrossAxisAlignment.CENTER, alignment=ft.MainAxisAlignment.CENTER), width=10000))