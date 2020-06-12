"""empty message

Revision ID: b0ee61e57197
Revises: 267eca2121ac
Create Date: 2020-06-12 22:52:39.930447

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b0ee61e57197'
down_revision = '267eca2121ac'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('notes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('topic', sa.String(length=200), nullable=True),
    sa.Column('contents', sa.String(length=500), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('person')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('person',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('topic', sa.VARCHAR(length=200), autoincrement=False, nullable=True),
    sa.Column('contents', sa.VARCHAR(length=500), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='person_pkey')
    )
    op.drop_table('notes')
    # ### end Alembic commands ###