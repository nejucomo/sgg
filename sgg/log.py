from functools import wraps
import logging



def bind_log(f):
    log = logging.getLogger(f.name)
    @wraps(f)
    def g(*a, **kw):
        return f(log, *a, **kw)
    return g

