from typing import Annotated, AsyncGenerator
from fastapi import Depends
from sqlalchemy.orm import mapped_column

from .database import get_session


intpk = Annotated[int, mapped_column(primary_key=True)]

gen_session = Annotated[AsyncGenerator, Depends(get_session)]
