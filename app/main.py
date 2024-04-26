import sys
sys.dont_write_bytecode = True # Disables pycache

import asyncio
import flet as ft
from WatchDogs.app import App

asyncio.run(ft.app_async(App))
