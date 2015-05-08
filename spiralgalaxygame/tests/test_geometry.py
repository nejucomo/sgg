import unittest
from math import pi

from spiralgalaxygame.geometry import Vector, Circle


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

    def test_eq(self):
        a = Vector(0.5 ** 0.5, 0.5 ** 0.5)
        b = Vector.from_angle_and_radius(pi/4, 1)

        self.assertEqual(a, b)

    def test_neg(self):
        a = Vector(0.5 ** 0.5, 0.5 ** 0.5)
        b = Vector.from_angle_and_radius(1.25*pi, 1)

        self.assertEqual(a, -b)

    def test_add(self):
        a = Vector(0.5 ** 0.5, 0.5 ** 0.5)
        b = Vector.from_angle_and_radius(1.25*pi, 1)
        c = Vector(0.0, 0.0)

        self.assertEqual(c, a + b)

    def test_sub(self):
        a = Vector(0.5 ** 0.5, 0.5 ** 0.5)
        b = Vector.from_angle_and_radius(pi/4, 1)
        c = Vector(0.0, 0.0)

        self.assertEqual(c, a - b)

    def test_mul(self):
        a = Vector(1.0, 1.0)
        b = Vector.from_angle_and_radius(pi/4, 1)

        self.assertEqual(a, b * (2**0.5))

    def test_div(self):
        a = Vector(1.0, 1.0)
        b = a / a.magnitude

        self.assertAlmostEqual(1.0, b.magnitude)
        self.assertAlmostEqual(a.angle, b.angle)
        self.assertAlmostEqual(0.5**0.5, b.x)
        self.assertAlmostEqual(0.5**0.5, b.y)


class CircleTests (unittest.TestCase):
    def setUp(self):
        v = Vector(3.0, 4.0)
        r = 5.0
        c = Circle(v, r)
        self.testdata = (c, v, r)

    def test_tupleness(self):
        c, v, r = self.testdata
        self.assertIsInstance(c, tuple)
        (v1, r1) = c

        self.assertIs(v, v1)
        self.assertEqual(r, r1)
        self.assertIs(v, c[0])
        self.assertEqual(r, c[1])

    def test_properties(self):
        c, v, r = self.testdata

        self.assertIs(v, c.center)
        self.assertEqual(r, c.radius)

    def test_overlaps(self):
        c, _, _ = self.testdata

        self.failUnless(c.overlaps(Circle(Vector(0.0,0.0), 0.0)))
        self.failIf(c.overlaps(Circle(Vector(-0.1,-0.1), 0.05)))
