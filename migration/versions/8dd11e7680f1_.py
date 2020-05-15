"""empty message

Revision ID: 8dd11e7680f1
Revises: 2743a7783868
Create Date: 2020-05-15 21:31:56.016243

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8dd11e7680f1'
down_revision = '2743a7783868'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('job', 'job_id', new_column_name='job_id_external', type_=sa.String())
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('job', 'job_id_external', new_column_name='job_id', type_=sa.Integer())
    # ### end Alembic commands ###
