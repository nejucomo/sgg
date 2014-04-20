"""Module for async operation composition in twisted."""

from functools import wraps


def check_is_then(d, expected, f, *args, **kw):

    @wraps(f)
    def check_then_continue(result):
        assert result is expected, 'Unexpected deferred result: found %r, expected %r' % (result, expected)
        return f(*args, **kw)

    return d.addCallback(check_then_continue)


def then(d, f, *args, **kw):
    return check_is_then(d, None, f, *args, **kw)
