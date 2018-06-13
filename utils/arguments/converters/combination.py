from utils.arguments.types import spacing
from utils.functional.composition import compose

def choose_any(conversions):
    def try_converters(x):
        exceptions = []
        for c in map(adjust_converter, conversions):
            try:
                return c(x)
            except Exception as ex:
                exceptions += [ex]
        exceptionsMessages = "\n".join(map(
            lambda ex: "{}- {}".format(" " * spacing * 2, ex), 
            exceptions)
        )
        raise Exception("There were exceptions trying to parse the value '{}':\n{}".format(
            x, exceptionsMessages
        ))

    return try_converters


def adjust_converter(converter):
    if isinstance(converter, list):
        return compose(converter)
    else:
        return converter
