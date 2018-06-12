from itertools import filterfalse
from sys import argv

from utils.arguments.parsing import from_list
from utils.arguments.types import OptionalArg, RequiredArg
from utils.string import isempty

class ArgsSchema:
    def __init__(self, name, description, argumentDefinitions):
        self.name = name
        self.description = description

        def isRequired(x): return isinstance(x, RequiredArg)
        def isOptional(x): return isinstance(x, OptionalArg)

        if any(map(lambda arg: not (isRequired(arg) or isOptional(arg)), argumentDefinitions)):
            raise Exception(
                'Some arguments are not instances of RequiredArg or OptionalArg')

        self.required = list(filter(isRequired, argumentDefinitions))
        self.optional = list(filter(isOptional, argumentDefinitions))
        self.all_args = self.required + self.optional

        self.has_required = len(self.required) > 0
        self.has_optional = len(self.optional) > 0

    def get_usage(self):
        return " ".join(filterfalse(isempty, [
            self.name,
            " ".join(map(lambda req: req.name, self.required)),
            " ".join(map(lambda opt: "[{}={}]".format(opt.name, opt.default), self.optional))
        ]))

    def get_args_description(self):
        def join_args(args):
            return "".join(map(str, args))

        return "\n".join(filterfalse(isempty, [
                "Required arguments:\n{}".format(join_args(self.required)),
                "Optional arguments:\n{}".format(join_args(self.optional))
        ]))

    def __str__(self):
        return "{}\n\nUsage:\n\t{}\n\n{}".format(
            self.description,
            self.get_usage(),
            self.get_args_description()
        )

    def parse_list(self, ls):
        return from_list(self, ls)

    def run(self, main, argv):
        if len(argv) <= 1:
           print(self)
        else:
            result = self.parse_list(argv[1:])

            if result.success:
                main(result.args)
            else:
                print(result)
                exit(1)