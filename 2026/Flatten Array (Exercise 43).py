def flatten(iterable):
    result = []
    for item in iterable:
        if type(item) == list:
            result.extend(flatten(item))
        elif item is not None:
            result.append(item)
    return result