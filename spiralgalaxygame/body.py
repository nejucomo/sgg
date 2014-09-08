from sgg.precondition import PreconditionError
from sgg.geometry import Circle
from sgg.sentinel import Enum


BodyKind = Enum(
    'star_white',
    'star_yellow',
    'star_red',
    'planet_blue',
    'planet_grey',
    'planet_green',
    'planet_brown',
    'black_hole',
    'dust_cloud',
    'gas_cloud',
    )


class Body (tuple):
    def __new__(cls, kind, circle):
        if not (kind in BodyKind and isinstance(circle, Circle)):
            raise PreconditionError(cls, kind, circle)

        super(Body, cls).__new__(cls, (kind, circle))

    @property
    def kind(self):
        return self[0]

    @property
    def circle(self):
        return self[1]

