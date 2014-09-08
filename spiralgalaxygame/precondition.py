class PreconditionError (TypeError):
    def __init__(self, callee, *args):
        TypeError.__init__(self, '{0.__name__}{1!r}'.format(callee, args))
