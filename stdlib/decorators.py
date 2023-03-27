def public(func):
    def public(*args, **kwargs):
        return func(*args, **kwargs)
    return public


def initialise(func):
    def constructor(*args, **kwargs):
        return func(*args, **kwargs)
    return constructor
