from sqladmin.authentication import AuthenticationBackend

from fastapi_login.exceptions import InvalidCredentialsException

from fastapi import Request

from ..user.auth.utils import get_access_token
from ..user.auth.manager import manager


class AdminAuth(AuthenticationBackend):

    async def login(self, request: Request) -> bool:
        form = await request.form()
        phone, password = form["username"], form["password"]

        try:
            token = await get_access_token(phone, password)
        except InvalidCredentialsException:
            return False

        request.session.update({"token": token})
        return True

    async def logout(self, request: Request) -> bool:
        request.session.clear()
        return True

    async def authenticate(self, request: Request) -> bool:
        token = request.session.get("token")

        if not token:
            return False

        user = await manager.get_current_user(token)

        return user.is_superuser


authentication_backend = AdminAuth(secret_key='')
