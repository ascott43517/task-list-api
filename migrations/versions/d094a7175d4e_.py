"""empty message

Revision ID: d094a7175d4e
Revises: 67381d0ccb5b
Create Date: 2022-11-08 01:05:34.967205

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd094a7175d4e'
down_revision = '67381d0ccb5b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('goal', sa.Column('goal_id', sa.Integer(), autoincrement=True, nullable=False))
    op.drop_column('goal', 'id')
    op.drop_constraint('task_goal_id_fkey', 'task', type_='foreignkey')
    op.create_foreign_key(None, 'task', 'goal', ['goal_id'], ['goal_id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'task', type_='foreignkey')
    op.create_foreign_key('task_goal_id_fkey', 'task', 'goal', ['goal_id'], ['id'])
    op.add_column('goal', sa.Column('id', sa.INTEGER(), server_default=sa.text("nextval('goal_id_seq'::regclass)"), autoincrement=True, nullable=False))
    op.drop_column('goal', 'goal_id')
    # ### end Alembic commands ###
