from fastapi import Depends
from typing import Annotated
from ..models import User
from .router import fastapi_users


current_user = fastapi_users.current_user(active=True)
current_superuser = fastapi_users.current_user(superuser=True, active=True)

superuser = Annotated[User, Depends(current_superuser)]
user = Annotated[User, Depends(current_user)]
