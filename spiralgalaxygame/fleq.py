_DELTA = 1e-9

def float_eq(a, b):
    if a == b:
        return True
    else:
        return abs(a-b) < _DELTA
