from flet import (
    Container
)


class Animal(Container):
    def __init__(self, *args, **kwargs):
        super().__init__(
            *args,
            **kwargs,
            border_radius=10,
        )
