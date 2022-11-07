"""empty message

Revision ID: 077609f0c5e7
Revises: 0f592f6941c5
Create Date: 2022-11-03 18:32:42.718252

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '077609f0c5e7'
down_revision = '0f592f6941c5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('task',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('title', sa.String(), nullable=True),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('completed_at', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('task')
    # ### end Alembic commands ###