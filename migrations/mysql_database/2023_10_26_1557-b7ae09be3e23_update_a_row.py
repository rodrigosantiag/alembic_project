"""Update a row

Revision ID: b7ae09be3e23
Revises:
Create Date: 2023-10-26 15:57:05.757225

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "b7ae09be3e23"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    sql = sa.text("UPDATE products SET slug = 'product_3_updated' WHERE id = 3")
    connection = op.get_bind()

    connection.execute(sql)


def downgrade() -> None:
    pass
