from functools import reduce
from itertools import filterfalse
from utils.functional.composition import composeif, compose_or

def multiline_to_singleline(string, strip=True, remove_emptylines=True):
    functions = [
        (remove_emptylines, lambda ls: filterfalse(isempty, ls)),
        (strip, lambda ls: map(str.strip, ls))
    ]

    lines = composeif(functions)(string.splitlines())

    return ' '.join(lines)

isempty = compose_or([str.isspace, "".__eq__])