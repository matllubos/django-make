import six


commands = {}


class CommandBase(type):
    def __new__(cls, *args, **kwargs):
        name, _, attrs = args

        abstract = attrs.pop('abstract', False)
        super_new = super(CommandBase, cls).__new__
        new_class = super_new(cls, *args, **kwargs)

        if name != 'NewBase' and not abstract:
            commands[new_class.name] = new_class
        return new_class


class BaseCommand(six.with_metaclass(CommandBase)):
    name = None
    description = None
    abstract = True

    def handle(self, *args, **kwargs):
        raise NotImplementedError
