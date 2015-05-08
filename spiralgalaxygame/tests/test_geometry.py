import unittest
from math import pi

from spiralgalaxygame.geometry import Vector


class VectorTests (unittest.TestCase):
    def test_tupleness(self):
        v = Vector(2.0, 3.0)
        self.assertIsInstance(v, tuple)
        (x, y) = v

        self.assertEqual(x, 2.0)
        self.assertEqual(y, 3.0)
        self.assertEqual(v[0], 2.0)
        self.assertEqual(v[1], 3.0)

    def test_radial_constructor(self):
        v = Vector.from_angle_and_radius(0.25 * pi, 2 ** 0.5)
        (x, y) = v

        self.assertAlmostEqual(x, 1)
        self.assertAlmostEqual(y, 1)

    def test_cartesian_properties(self):
        v = Vector(2.0, 3.0)
        (x, y) = v

        self.assertEqual(x, v.x)
        self.assertEqual(y, v.y)

    def test_radial_properties(self):
        for i in range(8):
            a = pi * (i-3) / 4
            r = 1.0

            v = Vector.from_angle_and_radius(a, r)

            self.assertAlmostEqual(a, v.angle)
            self.assertAlmostEqual(r, v.magnitude)

    def test_angle_edge_cases(self):
        self.assertAlmostEqual(pi/2, Vector(0.0,1.0).angle)
        self.assertAlmostEqual(-pi/2, Vector(0.0,-1.0).angle)

    def test_repr(self):
        self.assertEqual('<2.0, 3.0>', repr(Vector(2.0, 3.0)))

