"""fixed

Revision ID: f534be345a91
Revises: e3a5b94c708b
Create Date: 2023-11-13 20:37:28.778464

"""
from typing import Sequence, Union

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision: str = "f534be345a91"
down_revision: Union[str, None] = "e3a5b94c708b"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column("client_tag", sa.Column("obj_id", sa.Integer()))
    op.drop_constraint(
        "client_tag_client_id_fkey", "client_tag", type_="foreignkey"
    )
    op.create_foreign_key(
        None, "client_tag", "clients", ["obj_id"], ["id"], ondelete="CASCADE"
    )
    op.drop_column("client_tag", "client_id")
    op.add_column("mailing_tag", sa.Column("obj_id", sa.Integer()))
    op.drop_constraint(
        "mailing_tag_mailing_id_fkey", "mailing_tag", type_="foreignkey"
    )
    op.create_foreign_key(
        None, "mailing_tag", "mailings", ["obj_id"], ["id"], ondelete="CASCADE"
    )
    op.drop_column("mailing_tag", "mailing_id")
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "mailing_tag",
        sa.Column("mailing_id", sa.INTEGER(), autoincrement=False),
    )
    op.drop_constraint(None, "mailing_tag", type_="foreignkey")
    op.create_foreign_key(
        "mailing_tag_mailing_id_fkey",
        "mailing_tag",
        "mailings",
        ["mailing_id"],
        ["id"],
        ondelete="CASCADE",
    )
    op.drop_column("mailing_tag", "obj_id")
    op.add_column(
        "client_tag", sa.Column("client_id", sa.INTEGER(), autoincrement=False)
    )
    op.drop_constraint(None, "client_tag", type_="foreignkey")
    op.create_foreign_key(
        "client_tag_client_id_fkey",
        "client_tag",
        "clients",
        ["client_id"],
        ["id"],
        ondelete="CASCADE",
    )
    op.drop_column("client_tag", "obj_id")
    # ### end Alembic commands ###
