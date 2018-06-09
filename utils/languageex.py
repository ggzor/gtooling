def applyif(val, f, condition):
    """
    Equivalent to: 
        f(val) if condition else val
    """
    return f(val) if condition else val

def value_or_raise_if(condition, exception_message, value):
    """
    Equivalent to:
        if condition:
            raise Exception(exception_message)
        return value        
    """
    if condition:
        raise Exception(exception_message)
    return value