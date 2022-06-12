"""Add items table

Revision ID: f8625586f1bd
Revises: 85d29da807d6
Create Date: 2022-06-12 00:08:55.302753

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f8625586f1bd'
down_revision = '85d29da807d6'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "items",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("title", sa.String(), nullable=True),
        sa.Column("description", sa.String(), nullable=True),
        sa.PrimaryKeyConstraint("id")
    )
    op.create_index(
        op.f("ix_items_id"),
        "items",
        ["id"],
        unique=False
    )
    op.create_index(
        op.f("ix_items_title"),
        "items",
        ["title"],
        unique=False
    )
    op.create_index(
        op.f("ix_items_description"),
        "items",
        ["description"],
        unique=False
    )


def downgrade() -> None:
    op.drop_index(op.f('ix_items_id'), table_name='items')
    op.drop_index(op.f('ix_items_title'), table_name='items')
    op.drop_index(op.f('ix_items_description'), table_name='items')
    op.drop_table("items")
