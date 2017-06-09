# pylint: disable=C0111,C0103,E1101

"""add-boolean-column

Revision ID: 726a4e34f2d2
Revises: aaf9576a71f6
Create Date: 2017-06-06 18:56:19.794244

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '726a4e34f2d2'
down_revision = 'aaf9576a71f6'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('user', sa.Column('is_admin', sa.Boolean))


def downgrade():
    with op.batch_alter_table('user') as batch_op:
        batch_op.drop_column('is_admin')
