from alembic import op
import sqlalchemy as sa

revision="0001"
down_revision=None
branch_labels=None
depends_on=None

def upgrade():
    op.create_table("users",
        sa.Column("id",sa.Integer(),primary_key=True),
        sa.Column("email",sa.String(length=255),nullable=False),
        sa.Column("password_hash",sa.String(length=255),nullable=False))
    op.create_index("ix_users_email","users",["email"],unique=True)
    op.create_table("tasks",
        sa.Column("id",sa.Integer(),primary_key=True),
        sa.Column("title",sa.String(length=200),nullable=False),
        sa.Column("description",sa.Text(),nullable=True),
        sa.Column("status",sa.String(length=30),nullable=False),
        sa.Column("created_at",sa.DateTime(),nullable=False),
        sa.Column("owner_id",sa.Integer(),sa.ForeignKey("users.id"),nullable=False))

def downgrade():
    op.drop_table("tasks")
    op.drop_index("ix_users_email",table_name="users")
    op.drop_table("users")
