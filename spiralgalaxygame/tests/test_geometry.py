import unittest
from math import pi

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

    def test_radial_constructor(self):
        v = Vector.from_angle_and_radius(0.25 * pi, 2 ** 0.5)
        (x, y) = v

        self.assertAlmostEqual(x, 1)
        self.assertAlmostEqual(y, 1)

    def test_cartesian_properties(self):
        v = Vector(2, 3)
        (x, y) = v

        self.assertEqual(x, v.x)
        self.assertEqual(y, v.y)

    def test_radial_properties(self):
        for i in range(8):
            a = pi * (i-3) / 8
            r = 42.0

            v = Vector.from_angle_and_radius(a, r)

            vangle = v.angle
            self.assertAlmostEqual(a, vangle, 7, `locals()`)
            self.assertAlmostEqual(r, v.magnitude, 7, `locals()`)

