"""add new columns for user

Revision ID: 34bae0ba69df
Revises: dc329e9aee78
Create Date: 2019-02-28 08:47:23.379625

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '34bae0ba69df'
down_revision = 'dc329e9aee78'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('about_me', sa.String(length=128), nullable=True))
    op.add_column('user', sa.Column('create_time', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'create_time')
    op.drop_column('user', 'about_me')
    # ### end Alembic commands ###
