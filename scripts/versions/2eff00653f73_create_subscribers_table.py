"""create_subscribers_table

Revision ID: 2eff00653f73
Revises: 
Create Date: 2019-06-07 09:37:36.118997

"""
from alembic import op
from uuid import uuid4
from sqlalchemy.dialects.postgresql import UUID

import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "2eff00653f73"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "subscribers",
        sa.Column("id", UUID(as_uuid=True), primary_key=True, default=uuid4),
        sa.Column("created_at", sa.DateTime, default=sa.func.now()),
        sa.Column("updated_at", sa.DateTime, nullable=True),
    )


def downgrade():
    op.drop_table("subscribers")
