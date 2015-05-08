import unittest

from spiralgalaxygame.geometry import Vector


class VectorTests (unittest.TestCase):
    def test_tupleness(self):
        v = Vector(2, 3)
        self.assertIsInstance(v, tuple)

        (x, y) = v
        self.assertEqual(x, 2)
        self.assertEqual(y, 3)
        self.assertEqual(v[0], 2)
        self.assertEqual(v[1], 3)
