from functools import wraps
import logging
from spiralgalaxygame import callee


def bind_logger(f):
    log = logging.getLogger(callee.name_of(f))
    @wraps(f)
    def g(*a, **kw):
        return f(log, *a, **kw)
    return g
