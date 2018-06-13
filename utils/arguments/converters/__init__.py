from utils.languageex import value_or_raise_if

def equals_to(value):
    return lambda x: value_or_raise_if(
        value != x,
            "The value '{}' is not equal to {}.".format(x, value),
        x
    )