class Sentinel (object):
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<%s %s>' % (self.__class__.__name__, self.name)


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
        return '<%s %s>' % (self.__class__.__name__, ', '.join(sorted( s.name for s in self )))


