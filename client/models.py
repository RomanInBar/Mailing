from database.engine import Base
from sqlalchemy import ForeignKey, String, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship
from utils.dependencies import current, pk, update


class ClientORM(Base):
    __tablename__ = 'clients'
    id: Mapped[pk]
    email: Mapped[str] = mapped_column(String(100), unique=True)
    create_at: Mapped[current]
    update_at: Mapped[update]
    tags_of_client: Mapped[list['TagORM']] = relationship(
        secondary='client_tag',
        back_populates='clients_of_tag',
        uselist=True,
        lazy='selectin',
    )

    def append_tag(self, tag):
        self.tags_of_client.append(tag)

    def remove_tag(self, tag):
        self.tags_of_client.remove(tag)


class ClientTagORM(Base):
    __tablename__ = 'client_tag'
    id: Mapped[pk]
    obj_id: Mapped[int] = mapped_column(
        ForeignKey('clients.id', ondelete='CASCADE')
    )
    tag_id: Mapped[int] = mapped_column(
        ForeignKey('tags.id', ondelete='CASCADE')
    )
    UniqueConstraint('client_id', 'tag_id', name='unique_client_tag')
