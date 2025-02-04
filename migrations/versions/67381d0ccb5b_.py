"""empty message

Revision ID: 67381d0ccb5b
Revises: 72c2edea218f
Create Date: 2022-11-06 23:30:45.538691

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '67381d0ccb5b'
down_revision = '72c2edea218f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('task', sa.Column('goal_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'task', 'goal', ['goal_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'task', type_='foreignkey')
    op.drop_column('task', 'goal_id')
    # ### end Alembic commands ###
