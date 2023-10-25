"""Add foobar row

Revision ID: 4423290da050
Revises:
Create Date: 2023-10-25 14:48:02.139020+00:00

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "4423290da050"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    sql = sa.text("INSERT INTO test_table_postgres (name) VALUES ('foo bar')")
    connection = op.get_bind()

    connection.execute(sql)


def downgrade() -> None:
    sql = sa.text("DELETE FROM test_table_postgres WHERE name = 'foo bar'")
    connection = op.get_bind()

    connection.execute(sql)
