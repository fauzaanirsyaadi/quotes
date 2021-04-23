"""empty message

Revision ID: dba66b10b5fa
Revises: 
Create Date: 2021-04-22 22:12:40.874193

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'dba66b10b5fa'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('quotes',
    sa.Column('quotes_id', sa.BigInteger(), autoincrement=True, nullable=False),
    sa.Column('quotes_value', sa.String(length=1000), nullable=False),
    sa.PrimaryKeyConstraint('quotes_id'),
    sa.UniqueConstraint('quotes_value')
    )
    op.create_table('users',
    sa.Column('users_id', sa.BigInteger(), autoincrement=True, nullable=False),
    sa.Column('users_name', sa.String(length=250), nullable=False),
    sa.Column('users_email', sa.String(length=100), nullable=False),
    sa.Column('users_password', sa.String(length=250), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('users_id')
    )
    op.create_index(op.f('ix_users_users_email'), 'users', ['users_email'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_users_users_email'), table_name='users')
    op.drop_table('users')
    op.drop_table('quotes')
    # ### end Alembic commands ###
