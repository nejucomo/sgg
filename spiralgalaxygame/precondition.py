from types import FunctionType, MethodType


class PreconditionError (TypeError):
    def __init__(self, callee, *args):
        if isinstance(callee, MethodType):
            name = '{0.im_class.__name__}.{0.im_func.__name__}'.format(callee)
        elif isinstance(callee, type) or isinstance(callee, FunctionType):
            name = callee.__name__

        TypeError.__init__(self, '{}{!r}'.format(name, args))
