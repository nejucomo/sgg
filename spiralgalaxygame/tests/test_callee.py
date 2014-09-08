import unittest

from spiralgalaxygame import callee


class calleeTests (unittest.TestCase):
    def test_str_of_func(self):
        def my_func(): pass

        self.assertEqual(callee.name_of(my_func), 'my_func')

    def test_str_of_type(self):
        class MyType (object): pass

        self.assertEqual(callee.name_of(MyType), 'MyType')

    def test_str_of_method(self):
        class MyType (object):
            def my_method(self):
                pass

        self.assertEqual(callee.name_of(MyType.my_method), 'MyType.my_method')

