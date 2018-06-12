from utils.languageex import value_or_raise_if

def to_integer(value):
    try:
        return int(value)
    except ValueError:
        raise ValueError("The value '{}' is not a valid integer.".format(value))

def positive_integer(value):
    return value_or_raise_if(
        value <= 0,
            "The value {} is not positive.".format(value),
        value
    )

def positive_integer_or_zero(value):
    if value < 0:
        positive_integer(value)
    return value