"""rename department

Revision ID: 92e20b702299
Revises: 8e00f7d3ea2c
Create Date: 2024-09-06 18:05:08.721153

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '92e20b702299'
down_revision = '8e00f7d3ea2c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.rename_table('department', 'departments')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.rename_table('departments', 'department')
    # ### end Alembic commands ###
