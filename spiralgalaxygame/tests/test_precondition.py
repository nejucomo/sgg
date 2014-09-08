import unittest

from spiralgalaxygame.precondition import PreconditionError


class PreconditionErrorTests (unittest.TestCase):
    def test_str_of_func(self):
        def my_func(): pass

        self.assertEqual(
            str(PreconditionError(my_func, 'banana', 'wombat')),
            "my_func('banana', 'wombat')")

    def test_str_of_type(self):
        class MyType (object): pass

        self.assertEqual(
            str(PreconditionError(MyType, 'banana', 'wombat')),
            "MyType('banana', 'wombat')")

    def test_str_of_method(self):
        class MyType (object):
            def my_method(self):
                pass

        self.assertEqual(
            str(PreconditionError(MyType.my_method, 'banana', 'wombat')),
            "MyType.my_method('banana', 'wombat')")

