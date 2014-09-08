from spiralgalaxygame import callee


class PreconditionError (TypeError):
    def __init__(self, obj, *args):
        TypeError.__init__(self, '{}{!r}'.format(callee.name_of(obj), args))
