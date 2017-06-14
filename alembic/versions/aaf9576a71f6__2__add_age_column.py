# pylint: disable=C0111,C0103,E1101

"""Add age column

Revision ID: aaf9576a71f6
Revises: 4468cd639356
Create Date: 2017-05-29 17:10:32.788779

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'aaf9576a71f6'
down_revision = '4468cd639356'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('user', sa.Column('age', sa.Integer))


def downgrade():
    with op.batch_alter_table('user') as batch_op:
        batch_op.drop_column('age')


