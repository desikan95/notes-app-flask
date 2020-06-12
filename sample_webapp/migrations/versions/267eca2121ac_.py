"""empty message

Revision ID: 267eca2121ac
Revises: 0ecf504a8889
Create Date: 2020-06-12 16:03:42.694311

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '267eca2121ac'
down_revision = '0ecf504a8889'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('person',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('topic', sa.String(length=200), nullable=True),
    sa.Column('contents', sa.String(length=500), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('notes')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('notes',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('topic', sa.VARCHAR(length=200), autoincrement=False, nullable=True),
    sa.Column('contents', sa.VARCHAR(length=500), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='notes_pkey')
    )
    op.drop_table('person')
    # ### end Alembic commands ###
