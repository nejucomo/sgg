import random
from math import sin, pi
from sgg.body import Body, BodyKind
from sgg.geometry import Vector, Circle
from sgg.discdist import DiscreteDistribution


def generate_galaxy_bodies(spokes = 4, spin = 3.8, diffusion = 13.5, tightness = 0.35):
    pass


# Notes:
#
# Parameters named u are expected to be uniform random samples on [0, 1).
#
# The "Standard Length Unit" is a convenient unit of measurement of
# game objects, where the smallest ships have a radius close to 1 SLU.

def generate_star(randgen, galacticradius, spokes, spin, diffusion, tightness):
    """randgen is a function which generates uniform random samples [0, 1)."""
    (kind, tightnessfactor, minrad, radrange, childmu, childsigma) = select_star_info(randgen())

    adjustedtightness = tightness * tightnessfactor

    bdfc = select_body_distance(galacticradius, adjustedtightness, randgen())
    angle = select_angle(spokes, diffusion, spin, bdfc, randgen())
    bodyradius = select_star_radius(minrad, radrange, randgen())

    circle = Circle(Vector.from_angle_and_radius(angle, bdfc), bodyradius)
    parent = Body(kind, circle)

    yield parent

    for i in range(int(random.lognormvariate(childmu, childsigma))):
        yield generate_child(randgen, circle)


def generate_child(randgen, pcircle):
    (kind, solarradius, minrad, radrange) = select_child_info(randgen())

    bdfp = pcircle.radius + select_body_distance(solarradius, tigthness = 0.5, u = randgen())
    angle = randgen * 2 * pi

    center = pcircle.center + Vector.from_angle_and_radius(angle, bdfp)
    bodyradius = select_star_radius(minrad, radrange)

    return Body(kind, Circle(center, bodyradius))


def select_body_distance(galacticradius, tightness, u):
    """Given galacticradius in SLUs, a tightness parameter, and a u sample, return a distance in SLUs."""
    t = sin(0.5 * pi * u) ** tightness
    k = (t + u**4) / 2
    return galacticradius * k


def select_angle(spokes, diffusion, spin, bdfc, u):
    """Given spokes, diffusion, spin, and bdfc (body distance from core) and a u, return galactic angle."""
    return select_base_angle(spokes, diffusion, spin, u) + spin * bdfc


def select_base_angle(spokes, diffusion, u):
    factor = spokes * pi
    a = sin(factor * u)
    b = abs(a) ** diffusion
    return u - b / factor


def select_star_radius(minradius, radiusrange, u):
    return minradius + radiusrange * u**2


select_star_info = DiscreteDistribution(
    # items: (kind, tightnessfactor, minrad, radrange, childmu, childsigma)
    # Note: blue and green planets are never parent bodies.
    (99, (BodyKind.star_white,   0.9,  100, 100,  0.35, 0.55)),
    (60, (BodyKind.star_yellow,  0.85, 80,  200,  0.50, 0.50)),
    (40, (BodyKind.star_red,     0.67, 40,  120,  0.20, 0.30)),
    (7,  (BodyKind.planet_grey,  1.0,  10,  80,  -0.50, 0.11)),
    (1,  (BodyKind.planet_brown, 0.9,  30,  40,  -0.40, 0.15)),
    (10, (BodyKind.black_hole,   0.4,  1,   10,  -0.30, 0.30)),
    (17, (BodyKind.dust_cloud,   1.0,  80,  400, -1.00, 0.00)),
    (13, (BodyKind.gas_cloud,    0.6,  80,  800, -1.00, 0.00)),
    )

select_child_info = DiscreteDistribution(
    # items: (kind, solarradius, minrad, radrange)
    # Note: dust clouds and gas clouds are never children.
    (1,   (BodyKind.star_white,   1000, 60, 100)),
    (1,   (BodyKind.star_yellow,  1100, 50, 130)),
    (2,   (BodyKind.star_red,     1300, 20, 50)),
    (100, (BodyKind.planet_blue,  1400, 10, 80)),
    (120, (BodyKind.planet_grey,  2500, 10, 60)),
    (90,  (BodyKind.planet_green, 1200, 15, 60)),
    (80,  (BodyKind.planet_brown, 1800, 25, 30)),
    (5,   (BodyKind.black_hole,   700,  1,  6)),
    )
