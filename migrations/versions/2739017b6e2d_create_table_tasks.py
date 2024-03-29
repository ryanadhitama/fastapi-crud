"""Create table tasks

Revision ID: 2739017b6e2d
Revises: 
Create Date: 2024-03-29 05:03:04.108937

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2739017b6e2d'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        "tasks",
        sa.Column("id", sa.INTEGER, nullable=False),
        sa.Column("name", sa.VARCHAR(100), nullable=False),
        sa.Column("description", sa.VARCHAR(100), nullable=True),
        sa.Column(
            "created_at",
            sa.TIMESTAMP,
            nullable=False,
            server_default=sa.text("now()"),
        ),
        sa.Column(
            "updated_at",
            sa.TIMESTAMP,
            nullable=True,
            server_default=sa.text("now()"),
            onupdate=sa.text("now()"),
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    pass


def downgrade() -> None:
    op.drop_table("tasks")
    pass
