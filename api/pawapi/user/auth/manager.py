from fastapi import Depends
from fastapi_login import LoginManager
from typing import Annotated

from ..models import User
from pawapi.config import settings


manager = LoginManager(settings.MANAGER_TOKEN, token_url='/auth/token')

current_user = Annotated[User, Depends(manager)]
