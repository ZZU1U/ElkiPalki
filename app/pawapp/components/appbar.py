from flet import AppBar, IconButton, icons, Text


def MyAppBar(title='Добрые руки', actions=None, back=None):
    if actions is None:
        actions = []

    return AppBar(
                leading=IconButton(icon=icons.ARROW_BACK, icon_size=20, on_click=back),
                leading_width=40,
                title=Text(title),
                actions=actions
            )