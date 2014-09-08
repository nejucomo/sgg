import unittest

from spiralgalaxygame.sentinel import Sentinel, Enum


class SentinelTests (unittest.TestCase):
    def setUp(self):
        self.s = Sentinel('thingy')

    def test_name(self):
        self.assertIs(self.s.name, 'thingy')

    def test_repr(self):
        self.assertEqual(repr(self.s), '<Sentinel thingy>')

    def test_identity_by_name(self):
        s2 = Sentinel('th' + 'ingy') # `+` to avoid string interning.
        self.assertIs(s2, self.s)


class EnumTests (unittest.TestCase):
    def setUp(self):
        self.e = Enum('red', 'green', 'blue')

    def test_iter_and_members_are_sentinels(self):
        for member in self.e:
            self.assertIsInstance(member, Sentinel)

    def test_member_as_attr_and_in_operator(self):
        self.assertIn(self.e.green, self.e)
