from types import MethodType


def name_of(callee):
    if isinstance(callee, MethodType):
        return '{0.im_class.__name__}.{0.im_func.__name__}'.format(callee)
    else:
        return callee.__name__
