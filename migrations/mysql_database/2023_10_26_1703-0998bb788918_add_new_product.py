"""Add new product

Revision ID: 0998bb788918
Revises: b7ae09be3e23
Create Date: 2023-10-26 17:03:17.301600

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "0998bb788918"
down_revision: Union[str, None] = "b7ae09be3e23"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    sql = sa.text("INSERT INTO products (name, slug) VALUES ('New Product', 'new_product')")

    connection = op.get_bind()
    connection.execute(sql)


def downgrade() -> None:
    pass
