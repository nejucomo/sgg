from math import atan, cos, pi, sin, sqrt
from preconditions import preconditions


class Vector (tuple):

    @classmethod
    def from_angle_and_radius(cls, angle, radius):
        return cls(radius * cos(angle), radius * sin(angle))

    @preconditions(
        lambda x: isinstance(x, float) or isinstance(x, int),
        lambda y: isinstance(y, float) or isinstance(y, int),
        )
    def __new__(cls, x, y):
        return super(Vector, cls).__new__(cls, (x, y))

    @property
    def x(self):
        return self[0]

    @property
    def y(self):
        return self[1]

    @property
    def angle(self):
        (x, y) = self
        if x == 0:
            return -pi/2 if y < 0 else pi/2
        elif x > 0:
            return atan(y/x)
        else:
            return (-pi if y < 0 else pi) + atan(y/x)

    @property
    def magnitude(self):
        return sqrt(self.x ** 2 + self.y ** 2)

    def __repr__(self):
        return '<{!r}, {!r}>'.format(*self)

    def __neg__(self):
        return Vector(-self.x, -self.y)

    @preconditions(
        lambda other: isinstance(other, Vector),
        )
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return self + (- other)

    @preconditions(
        lambda other: isinstance(other, float),
        )
    def __mul__(self, other):
        return self + (- other)


class Circle (tuple):

    @preconditions(
        lambda center: isinstance(center, Vector),
        lambda radius: isinstance(radius, float) and radius >= 0,
        )
    def __new__(cls, center, radius):
        return super(Circle, cls).__new__(cls, (center, radius))

    @property
    def center(self):
        return self[0]

    @property
    def radius(self):
        return self[1]

    @preconditions(
        lambda other: isinstance(other, Circle),
        )
    def overlaps(self, other):
        return (self.center - other.center).magnitude <= (self.radius + other.radius)


