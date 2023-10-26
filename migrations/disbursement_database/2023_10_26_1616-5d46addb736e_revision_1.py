"""Revision 1

Revision ID: 5d46addb736e
Revises:
Create Date: 2023-10-26 16:16:06.181165

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "5d46addb736e"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    sql = sa.text(
        "INSERT INTO disbursals (id, name, street_name, period, amount) "
        "VALUES ('9ae2d203-9737-4fff-8902-5780d2288fe0', 'name 1', 'street 1', 8, 130.0)"
    )

    connection = op.get_bind()

    connection.execute(sql)


def downgrade() -> None:
    pass
