from sgg.precondition import PreconditionError


class DiscreteDistribution (object):

    def __init__(self, *weighteditems):
        self._total = 0.0

        for (weight, _) in weighteditems:
            self._total += weight

        self._weighteditems = weighteditems

    def __call__(self, u):
        if not (isinstance(u, float) and 0 <= u < 1.0):
            raise PreconditionError(self.__call__, u)

        k = u * self._total

        for (weight, item) in self._weighteditems:
            k -= weight
            if k < 0:
                return item

        assert False, 'Invariant failed: k {!r}, u {!r}, items {!r}'.format(k, u, self._weighteditems)
