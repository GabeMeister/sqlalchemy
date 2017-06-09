# pylint: disable=C0111,C0103,E1101

"""initial db commit

Revision ID: 4468cd639356
Revises:
Create Date: 2017-05-29 15:41:07.102279

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4468cd639356'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('user',\
        sa.Column('id', sa.Integer, primary_key=True),\
        sa.Column('name', sa.String(50), nullable=False))


def downgrade():
    op.drop_table('user')
