"""Update a row

Revision ID: 58bc442c825f
Revises:
Create Date: 2023-10-26 12:18:35.238123

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "58bc442c825f"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    sql = sa.text(
        "INSERT INTO public.public_table (name, amount, period) VALUES ('Migration 1', 234.90, 9)"
    )
    connection = op.get_bind()

    connection.execute(sql)


def downgrade() -> None:
    pass
