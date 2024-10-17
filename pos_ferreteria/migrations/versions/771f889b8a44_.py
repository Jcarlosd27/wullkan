"""empty message

Revision ID: 771f889b8a44
Revises: 613c251bce44
Create Date: 2024-10-07 19:36:37.678261

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '771f889b8a44'
down_revision = '613c251bce44'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('clients', schema=None) as batch_op:
        batch_op.alter_column('id',
               existing_type=sa.INTEGER(),
               nullable=False,
               autoincrement=True)
        batch_op.alter_column('company_name',
               existing_type=sa.TEXT(),
               type_=sa.String(length=150),
               existing_nullable=False,
               existing_server_default=sa.text("'Sin Nombre'"))
        batch_op.alter_column('rut',
               existing_type=sa.TEXT(),
               type_=sa.String(length=50),
               existing_nullable=False,
               existing_server_default=sa.text("'99999999-9'"))
        batch_op.alter_column('legal_representative',
               existing_type=sa.TEXT(),
               type_=sa.String(length=150),
               existing_nullable=False,
               existing_server_default=sa.text("'Sin Representante'"))
        batch_op.alter_column('address',
               existing_type=sa.TEXT(),
               type_=sa.String(length=200),
               existing_nullable=False,
               existing_server_default=sa.text("'Sin Dirección'"))
        batch_op.alter_column('region',
               existing_type=sa.TEXT(),
               type_=sa.String(length=100),
               existing_nullable=False,
               existing_server_default=sa.text("'Sin Región'"))
        batch_op.alter_column('commune',
               existing_type=sa.TEXT(),
               type_=sa.String(length=100),
               existing_nullable=False,
               existing_server_default=sa.text("'Sin Comuna'"))
        batch_op.alter_column('contact_number',
               existing_type=sa.TEXT(),
               type_=sa.String(length=50),
               existing_nullable=False,
               existing_server_default=sa.text("'000000000'"))
        batch_op.alter_column('landline',
               existing_type=sa.TEXT(),
               type_=sa.String(length=50),
               existing_nullable=True)
        batch_op.alter_column('approved_credit_amount',
               existing_type=sa.REAL(),
               type_=sa.Float(),
               existing_nullable=False,
               existing_server_default=sa.text('(0.0)'))
        batch_op.alter_column('branch',
               existing_type=sa.TEXT(),
               type_=sa.String(length=100),
               existing_nullable=True)
        batch_op.alter_column('associated_seller',
               existing_type=sa.TEXT(),
               type_=sa.String(length=100),
               existing_nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('clients', schema=None) as batch_op:
        batch_op.alter_column('associated_seller',
               existing_type=sa.String(length=100),
               type_=sa.TEXT(),
               existing_nullable=True)
        batch_op.alter_column('branch',
               existing_type=sa.String(length=100),
               type_=sa.TEXT(),
               existing_nullable=True)
        batch_op.alter_column('approved_credit_amount',
               existing_type=sa.Float(),
               type_=sa.REAL(),
               existing_nullable=False,
               existing_server_default=sa.text('(0.0)'))
        batch_op.alter_column('landline',
               existing_type=sa.String(length=50),
               type_=sa.TEXT(),
               existing_nullable=True)
        batch_op.alter_column('contact_number',
               existing_type=sa.String(length=50),
               type_=sa.TEXT(),
               existing_nullable=False,
               existing_server_default=sa.text("'000000000'"))
        batch_op.alter_column('commune',
               existing_type=sa.String(length=100),
               type_=sa.TEXT(),
               existing_nullable=False,
               existing_server_default=sa.text("'Sin Comuna'"))
        batch_op.alter_column('region',
               existing_type=sa.String(length=100),
               type_=sa.TEXT(),
               existing_nullable=False,
               existing_server_default=sa.text("'Sin Región'"))
        batch_op.alter_column('address',
               existing_type=sa.String(length=200),
               type_=sa.TEXT(),
               existing_nullable=False,
               existing_server_default=sa.text("'Sin Dirección'"))
        batch_op.alter_column('legal_representative',
               existing_type=sa.String(length=150),
               type_=sa.TEXT(),
               existing_nullable=False,
               existing_server_default=sa.text("'Sin Representante'"))
        batch_op.alter_column('rut',
               existing_type=sa.String(length=50),
               type_=sa.TEXT(),
               existing_nullable=False,
               existing_server_default=sa.text("'99999999-9'"))
        batch_op.alter_column('company_name',
               existing_type=sa.String(length=150),
               type_=sa.TEXT(),
               existing_nullable=False,
               existing_server_default=sa.text("'Sin Nombre'"))
        batch_op.alter_column('id',
               existing_type=sa.INTEGER(),
               nullable=True,
               autoincrement=True)

    # ### end Alembic commands ###