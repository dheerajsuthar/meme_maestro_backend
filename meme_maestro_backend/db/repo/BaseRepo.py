import importlib


class BaseRepo:
    @classmethod
    def get_model(cls):
        model = cls.__name__.replace('Repo', 'Model')
        module = importlib.import_module('.model', 'meme_maestro_backend.db')
        return getattr(module, model)

    @classmethod
    def create(cls, attribs):
        return getattr(cls.get_model(), 'create')(**attribs)

    # TODO: resume here tomorrow
    @classmethod
    def get(cls, id):
        return getattr(cls.get_model(), 'get')()

    def process_where_args(self, cls_, args):
        pass
