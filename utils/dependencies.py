from datetime import datetime
from typing import Annotated

from sqlalchemy.orm import mapped_column

pk = Annotated[int, mapped_column(primary_key=True, autoincrement=True)]
current = Annotated[datetime, mapped_column(default=datetime.utcnow)]
update = Annotated[
    datetime, mapped_column(default=datetime.utcnow, onupdate=datetime.utcnow)
]
