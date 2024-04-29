import sys
sys.dont_write_bytecode = True  # Disables pycache

import flet as ft
from pawapp.app import App

ft.app(App, port=8550, view=ft.AppView.FLET_APP_WEB)
