import flet as ft
import os
from flet.auth.providers import GoogleOAuthProvider


def registr(App):
    provider = GoogleOAuthProvider(client_id=os.getenv("GOOGLE_CLIENT_ID"),
        client_secret=os.getenv("GOOGLE_CLIENT_SECRET"),
        redirect_url="http://localhost:8550/api/oauth/redirect",)

    def login_click(e):
        App.page.login(provider)

    def on_login(e):
        print("Access token:", App.page.auth.token.access_token)
        print("User ID:", App.page.auth.user.id)

    App.page.on_login = on_login
    return ft.Column(controls=[ft.ElevatedButton("Login with Google", on_click=login_click)])