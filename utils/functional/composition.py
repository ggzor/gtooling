from functools import reduce

def compose(functions_list):
    '''
    Composes all the functions in the list starting with the rightmost.
    '''

    def reverse_composition(f, g):
        return lambda x: g(f(x))

    return reduce(reverse_composition, reversed(functions_list), lambda x: x)

def composeif(functions_list):
    '''
    Composes conditionally the function of each (compose, function) pair in the list 
    starting with the rightmost, only if bool(compose) == True.
    '''

    def reverse_conditional_composition(f, gt):
        return (lambda x: gt[1](f(x))) if gt[0] else f

    return reduce(reverse_conditional_composition, reversed(functions_list), lambda x: x)

def compose_and(functions_list):
    def compose_with(func):
        def composition(f, g):
            return lambda x: func(f(x), g(x))
        
        return composition

    return reduce(compose_with(lambda a,b: a and b), functions_list, lambda x: True)