"""verificatiion

Revision ID: 887fface666d
Revises: f786974b2dbe
Create Date: 2024-04-24 21:25:01.193387

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '887fface666d'
down_revision = 'f786974b2dbe'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('verification',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('passport', sa.String(length=255), nullable=True),
    sa.Column('valid_identification', sa.String(length=255), nullable=True),
    sa.Column('tax_statement', sa.String(length=255), nullable=True),
    sa.Column('bank_statement', sa.String(length=255), nullable=True),
    sa.Column('reference', sa.String(length=255), nullable=True),
    sa.Column('relationship', sa.String(length=255), nullable=True),
    sa.Column('reference_contact', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('verification')
    # ### end Alembic commands ###