"""empty message

Revision ID: a75237630b7a
Revises: 
Create Date: 2023-12-11 21:13:21.216493

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a75237630b7a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('superheros',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.Column('last_updated', sa.TIMESTAMP(), nullable=True),
    sa.Column('created_on', sa.TIMESTAMP(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_superheros_id'), 'superheros', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_superheros_id'), table_name='superheros')
    op.drop_table('superheros')
    # ### end Alembic commands ###
