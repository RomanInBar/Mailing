"""added UniqyeConstraint in the ClientTagORM model

Revision ID: 00a717987cd3
Revises: bc55b76de3c7
Create Date: 2023-11-13 15:46:29.497552

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '00a717987cd3'
down_revision: Union[str, None] = 'bc55b76de3c7'
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
