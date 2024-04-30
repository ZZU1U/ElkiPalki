from sqladmin.authentication import AuthenticationBackend
from fastapi import Request, HTTPException
from werkzeug.security import check_password_hash

from ..user.auth.database import load_user
from ..user.auth.manager import manager
from ..config import settings


class AdminAuth(AuthenticationBackend):

    async def login(self, request: Request) -> bool:
        form = await request.form()
        phone, password = form["username"], form["password"]

        user = await load_user(phone)
        if user is None or not check_password_hash(user.hashed_password, password):
            return False

        token = manager.create_access_token(
            data=dict(sub=phone)
        )

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
