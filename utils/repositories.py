from client.models import ClientORM, ClientTagORM
from tag.models import TagORM
from mailing.models import MailingORM, MailingTagORM, MessageORM
from utils.manager import ObjectManager


class Repository(ObjectManager):
    model = None


class TagRepository(ObjectManager):
    model = TagORM
