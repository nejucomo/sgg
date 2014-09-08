Sentinels = {}


class Sentinel (object):
    def __new__(cls, name):
        try:
            return Sentinels[name]
        except KeyError:
            s = object.__new__(cls)
            s.__init__(name)
            Sentinels[name] = s
            return s

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<{0.__class__.__name__} {0.name}>'.format(self)


class Enum (frozenset):
    def __new__(cls, *membernames):
        members = {}
        for name in membernames:
            members[name] = Sentinel(name)
        obj = super(Enum, cls).__new__(cls, members.values())
        for (name, member) in members.iteritems():
            setattr(obj, name, member)
        return obj

    def __repr__(self):
        return '<{0.__class__.__name__} {1}>'.format(self, ', '.join(sorted( s.name for s in self )))


