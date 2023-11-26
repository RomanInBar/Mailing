from sqlalchemy import UniqueConstraint, ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column
from database.engine import Base
import enum

from utils.dependencies import pk, current, update


class Status(enum.Enum):
    passed = 'PASSED',
    failed = 'FAILED'


class MailingORM(Base):
    __tablename__ = 'mailings'
    id: Mapped[pk]
    start: Mapped[current]
    message: Mapped[str]
    create_at: Mapped[current]
    tags_of_mailing: Mapped[list['TagORM']] = relationship(secondary='mailing_tag', back_populates='mailings_of_tag', uselist=True, lazy='selectin')

    def append_tag(self, tag):
        self.tags_of_mailing.append(tag)

    def remove_tag(self, tag):
        self.tags_of_mailing.remove(tag)


class MessageORM(Base):
    __tablename__ = 'messages'
    id: Mapped[pk]
    mailing_id: Mapped[int] = mapped_column(ForeignKey('mailings.id', ondelete='SET NULL'))
    client_id: Mapped[int] = mapped_column(ForeignKey('clients.id', ondelete='SET NULL'))
    send_at: Mapped[current]
    status: Mapped['Status']


class MailingTagORM(Base):
    __tablename__ = 'mailing_tag'
    id: Mapped[pk]
    obj_id: Mapped[int] = mapped_column(ForeignKey('mailings.id', ondelete='CASCADE'))
    tag_id: Mapped[int] = mapped_column(ForeignKey('tags.id', ondelete='CASCADE'))
    UniqueConstraint(
        'mailing_id',
        'tag_id',
        name='unique_mailing_tag'
    )
