"""fixed maooing types

Revision ID: 8b9aa4e66a9f
Revises: 14a15097da2a
Create Date: 2023-11-13 17:23:00.452135

"""
from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = "8b9aa4e66a9f"
down_revision: Union[str, None] = "14a15097da2a"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###
