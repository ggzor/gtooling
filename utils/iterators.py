def index(iterable, start=0):
    return zip(range(start, len(iterable) + start), iterable)