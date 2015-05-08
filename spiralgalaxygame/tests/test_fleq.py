import unittest
from math import sqrt

from spiralgalaxygame.fleq import float_eq


class fleqTests (unittest.TestCase):
    def test_float_eq_identity(self):
        a = 1.2
        self.failUnless(float_eq(a, a))

    def test_float_eq_literal(self):
        self.failUnless(float_eq(1.2, 1.2))

    def test_float_eq_computed(self):
        self.failUnless(float_eq(2 ** 0.5000000001, sqrt(2.000000001)))
