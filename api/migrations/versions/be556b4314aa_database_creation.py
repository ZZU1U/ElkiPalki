"""Database creation

Revision ID: be556b4314aa
Revises: 
Create Date: 2024-05-02 22:07:27.735817

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils.types.password
import sqlalchemy_utils.types.phone_number

# revision identifiers, used by Alembic.
revision: str = 'be556b4314aa'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('animal',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('species', sa.String(), nullable=False),
    sa.Column('age', sa.Integer(), nullable=False),
    sa.Column('description', sa.String(), nullable=False),
    sa.Column('image', sa.String(), nullable=True),
    sa.Column('status', sa.Enum('available', 'adopted', 'overexposed', 'unavailable', name='animalstatus'), nullable=False),
    sa.Column('last_donation', sa.DateTime(), nullable=True),
    sa.Column('food_donated', sa.Integer(), nullable=True),
    sa.Column('food_daily', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('password', sqlalchemy_utils.types.password.PasswordType(), nullable=False),
    sa.Column('phone', sqlalchemy_utils.types.phone_number.PhoneNumberType(), nullable=False),
    sa.Column('is_volunteer', sa.Boolean(), nullable=False),
    sa.Column('is_superuser', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('phone')
    )
    op.create_table('walk',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('date', sa.DateTime(timezone=True), nullable=False),
    sa.Column('duration', sa.Integer(), nullable=False),
    sa.Column('animal_id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['animal_id'], ['animal.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('walk')
    op.drop_table('user')
    op.drop_table('animal')
    # ### end Alembic commands ###