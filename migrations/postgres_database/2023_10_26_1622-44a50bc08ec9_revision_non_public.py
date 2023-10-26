"""Revision non_public

Revision ID: 44a50bc08ec9
Revises: 58bc442c825f
Create Date: 2023-10-26 16:22:40.804106

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "44a50bc08ec9"
down_revision: Union[str, None] = "58bc442c825f"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    sql = sa.text(
        "INSERT INTO non_public.non_public_table (external_id, result) "
        "VALUES ('foo_bar_extenal_id', 'denied')"
    )

    connection = op.get_bind()
    connection.execute(sql)


def downgrade() -> None:
    pass
