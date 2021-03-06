"""acronym max_length from 16 to 25

Revision ID: a1645606de5
Revises: 47996bf2842d
Create Date: 2015-05-29 16:21:01.160758

"""

# revision identifiers, used by Alembic.
revision = 'a1645606de5'
down_revision = '47996bf2842d'

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('meeting', 'acronym',
               existing_type=sa.VARCHAR(length=16),
               type_=sa.String(length=25),
               existing_nullable=False)
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('meeting', 'acronym',
               existing_type=sa.String(length=25),
               type_=sa.VARCHAR(length=16),
               existing_nullable=False)
    ### end Alembic commands ###
