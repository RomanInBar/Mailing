from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from database.engine import Base
from utils.dependencies import pk


class TagORM(Base):
    __tablename__ = "tags"
    id: Mapped[pk]
    name: Mapped[str] = mapped_column(String(100), unique=True)
    clients_of_tag: Mapped[list["ClientORM"]] = relationship(
        secondary="client_tag",
        back_populates="tags_of_client",
        uselist=True,
        lazy="selectin",
    )
    mailings_of_tag: Mapped[list["MailingORM"]] = relationship(
        secondary="mailing_tag",
        back_populates="tags_of_mailing",
        uselist=True,
        lazy="selectin",
    )
