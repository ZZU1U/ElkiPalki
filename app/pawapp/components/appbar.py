from flet import AppBar, IconButton, icons, Text


class MyAppBar(AppBar):
    def __init__(self, title='Добрые руки', actions=None, bgcolor='orange', back=None, **kwargs):
        if actions is None:
            actions = []
        super().__init__(
            leading=IconButton(icon=icons.ARROW_BACK, icon_size=20, on_click=back),
            leading_width=40,
            title=Text(title),
            actions=actions,
            bgcolor=bgcolor,
            **kwargs
        )