from utils.arguments.types import spacing

class ErrorArgs:
    def __init__(self, description, args):
        self.description = description
        self.args = args
        self.success = False

    def __str__(self):
        return "{}\n{}".format(
            self.description,
            "\n".join(map(self.format_arg, self.args))
        ) 
    
    def format_arg(self, arg):
        raise NotImplementedError

class MergedResult:
    def __init__(self, results):
        self.results = results
        self.success = False

    def __getattribute__(self, att):
        if att in ['results', 'success']:
            return object.__getattribute__(self, att)

        for r in self.results:
            try:
                return r.__getattribute__(att)
            except AttributeError:
                pass
        
        raise AttributeError(att)

    def __str__(self):
        return "\n".join(map(str, self.results))

class Success:
    def __init__(self, args):
        self.args = list(args)
        self.success = True

class DuplicatedArgs(ErrorArgs):
    def __init__(self, duplicated_args):
        self.duplicated_args = duplicated_args
        ErrorArgs.__init__(self, "There are duplicated args:", duplicated_args)

    def format_arg(self, arg):
        return "{}- {}: {}".format(" " * spacing, arg[0].name, ", ".join(arg[1]))

    def __str__(self):
        return ErrorArgs.__str__(self)

class MissingArgs(ErrorArgs):
    def __init__(self, missing_args):
        self.missing_args = missing_args
        ErrorArgs.__init__(self, "There are missing required args:", missing_args)

    def format_arg(self, arg):
        return str(arg)

    def __str__(self):
        return ErrorArgs.__str__(self)

class InvalidArgs(ErrorArgs):
    def __init__(self, invalid_args):
        self.invalid_args = invalid_args
        ErrorArgs.__init__(self, "There are invalid args:", invalid_args)

    def format_arg(self, arg):
        return "{}- {}: {}".format(" " * spacing, arg[0].name, arg[1])

    def __str__(self):
        return ErrorArgs.__str__(self)

class UnrecognizedArgs:
    def __init__(self, unrecognized_args):
        self.unrecognized_args = unrecognized_args
        ErrorArgs.__init__(self, "There are unrecognized args:", unrecognized_args)

    def format_arg(self, arg):
        return "{}- {}: {}".format(" " * spacing, arg[0], arg[1])

    def __str__(self):
        return ErrorArgs.__str__(self)