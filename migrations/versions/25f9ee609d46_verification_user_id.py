"""verification-user_id

Revision ID: 25f9ee609d46
Revises: 
Create Date: 2024-04-25 02:28:34.023974

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '25f9ee609d46'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('firstname', sa.String(), nullable=False),
    sa.Column('lastname', sa.String(), nullable=False),
    sa.Column('middlename', sa.String(), nullable=True),
    sa.Column('dob', sa.DateTime(), nullable=False),
    sa.Column('phone_number', sa.String(), nullable=False),
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('business_name', sa.String(), nullable=True),
    sa.Column('business_sector', sa.String(), nullable=True),
    sa.Column('registration_no', sa.String(), nullable=True),
    sa.Column('bvn', sa.String(), nullable=True),
    sa.Column('business_address', sa.String(), nullable=True),
    sa.Column('home_address', sa.String(), nullable=True),
    sa.Column('state', sa.String(), nullable=True),
    sa.Column('local_government', sa.String(), nullable=True),
    sa.Column('password', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('loan',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('loan_type', sa.String(), nullable=False),
    sa.Column('loan_amount', sa.String(), nullable=False),
    sa.Column('tenure', sa.Integer(), nullable=False),
    sa.Column('repayment_source', sa.String(), nullable=False),
    sa.Column('bank', sa.String(), nullable=False),
    sa.Column('account_name', sa.String(), nullable=False),
    sa.Column('account_type', sa.String(), nullable=False),
    sa.Column('account_no', sa.String(), nullable=False),
    sa.Column('driver_license', sa.String(), nullable=False),
    sa.Column('bvn', sa.String(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('verification',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('passport', sa.String(length=255), nullable=True),
    sa.Column('valid_identification', sa.String(length=255), nullable=True),
    sa.Column('tax_statement', sa.String(length=255), nullable=True),
    sa.Column('bank_statement', sa.String(length=255), nullable=True),
    sa.Column('reference', sa.String(length=255), nullable=True),
    sa.Column('relationship', sa.String(length=255), nullable=True),
    sa.Column('reference_contact', sa.String(length=255), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('verification')
    op.drop_table('loan')
    op.drop_table('user')
    # ### end Alembic commands ###
