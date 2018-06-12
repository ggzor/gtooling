from utils.functional.composition import compose

spacing = 4

def prepareConverter(converter):
    if isinstance(converter, list):
        return compose(converter)
    elif converter == None:
        return lambda x: x
    else:
        return converter

class RequiredArg:
    def __init__(self, name, description=None, converter=lambda x: x):
        self.name = str(name)
        self.description = description
        self.converter = prepareConverter(converter)

    def is_required(self):
        return True

    def __str__(self):
        return "{}- {}:\n{}{}\n".format(
            " " * spacing, 
            self.name,
            " " * spacing * 2,
            self.description
        )

class OptionalArg:
    def __init__(self, name, default, description=None, converter=lambda x: x):
        self.name = str(name)
        self.description = description
        self.converter = prepareConverter(converter)
        self.default = default

    def is_required(self):
        return False

    def __str__(self):
        return "{}- {}: (default = {})\n{}{}\n".format(
            " " * spacing, 
            self.name, self.default, 
            " " * spacing * 2,
            self.description
        )