from functools import reduce

def compose_monoid(identity_function, binary_function):
    '''
    Creates a function that composes a list of functions using binary_function from
    right to left, starting with the identity_function.
    '''
    def apply(current, next):
        return lambda x: binary_function(next, current)(x)

    return lambda functions_list: reduce(apply, reversed(functions_list), identity_function)

compose = compose_monoid(lambda x: x, 
    lambda f, g: lambda x: 
        f(g(x))
)

composeif = compose_monoid(lambda x: x, 
    lambda ft, g: lambda x: 
        ft[1](g(x)) if ft[0] else g(x)
)

compose_and = compose_monoid(lambda x: True, 
    lambda f, g: lambda x: 
        f(x) and g(x)
)

compose_or = compose_monoid(lambda x: False, 
    lambda f, g: lambda x: 
        f(x) or g(x)
)