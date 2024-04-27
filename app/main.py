import sys
sys.dont_write_bytecode = True  # Disables pycache

import asyncio
import flet as ft
from pawapp.app import App

asyncio.run(ft.app_async(App, port=8550, view=ft.AppView.FLET_APP))
