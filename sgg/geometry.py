from math import sqrt, cos, sin


class Vector (tuple):

    @classmethod
    def from_angle_and_radius(cls, angle, radius):
        return cls(radius * cos(angle), radius * sin(angle))

    def __new__(cls, x, y):
        if not (isinstance(x, float) and isinstance(y, float)):
            raise TypeError('%s(%r, %r)' % (cls.__name__, x, y))

        return super(Vector, cls).__new__(cls, (x, y))

    @property
    def x(self):
        return self[0]

    @property
    def y(self):
        return self[1]

    @property
    def magnitude(self):
        return sqrt(self.x ** 2 + self.y ** 2)

    def __repr__(self):
        return '<%r, %r>' % self

    def __neg__(self):
        return Vector(-self.x, -self.y)

    def __add__(self, other):
        if not isinstance(other, Vector):
            raise TypeError('%r + %r' % (self, other))
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return self + (- other)

    def __mul__(self, other):
        if not isinstance(other, float):
            raise TypeError('%r * %r' % (self, other))
        return self + (- other)


class Circle (tuple):
    def __new__(cls, center, radius):
        if not (isinstance(center, Vector) and isinstance(radius, float)):
            raise TypeError('%s(%r, %r)' % (cls.__name__, center, radius))

        return super(Circle, cls).__new__(cls, (center, radius))

    @property
    def center(self):
        return self[0]

    @property
    def radius(self):
        return self[1]

    def overlaps(self, other):
        if not isinstance(other, Circle):
            raise TypeError('%r.overlaps(%r)' % (self, other))

        return (self.center - other.center).magnitude <= (self.radius + other.radius)
