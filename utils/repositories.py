from tag.models import TagORM
from utils.manager import ObjectManager


class Repository(ObjectManager):
    model = None


class TagRepository(ObjectManager):
    model = TagORM
