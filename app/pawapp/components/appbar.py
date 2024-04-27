from flet import AppBar, IconButton, icons, Text, Image


class MyAppBar(AppBar):
    def __init__(self, title='Добрые руки', actions=None, bgcolor='orange', back=None, image=None, **kwargs):
        if actions is None:
            actions = []
        super().__init__(
            leading=IconButton(icon=icons.ARROW_BACK, icon_size=20, on_click=back),
            leading_width=40,
            title=Text(title) if image is None else Image(image),
            actions=actions,
            bgcolor=bgcolor,
            **kwargs
        )
