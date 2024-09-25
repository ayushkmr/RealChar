"""Add OpenAI Assistant ID column

Revision ID: 2ff034351a01
Revises: f31858d2a771
Create Date: 2024-09-25 18:12:23.267027

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2ff034351a01'
down_revision = 'f31858d2a771'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.add_column('characters', sa.Column('openai_assistant_id', sa.String(length=100), nullable=True))

def downgrade() -> None:
    op.drop_column('characters', 'openai_assistant_id')
