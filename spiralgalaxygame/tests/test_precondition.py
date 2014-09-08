import unittest

from spiralgalaxygame.precondition import PreconditionError

from mock import patch, sentinel


class PreconditionErrorTests (unittest.TestCase):

    @patch('spiralgalaxygame.callee.name_of')
    def test_init(self, m_name_of):
        PreconditionError(sentinel.target, sentinel.arg1, sentinel.arg2)
        self.failUnless(m_name_of.called_with(sentinel.target))

