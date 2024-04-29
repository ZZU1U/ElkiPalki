from fastapi_users.authentication import AuthenticationBackend

from .bearer import bearer_transport
from .strategy import get_database_strategy
from pawapi.config import settings


SECRET = settings.BACKEND_TOKEN

auth_backend = AuthenticationBackend(
    name="db",
    transport=bearer_transport,
    get_strategy=get_database_strategy,
)
