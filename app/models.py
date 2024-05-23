import sqlalchemy as sa
import sqlalchemy.orm as so
from app import db


class Log(db.Model):
    id: so.Mapped[int] = so.mapped_column(sa.Integer, primary_key=True)
    filename: so.Mapped[str] = so.mapped_column(sa.String)
    