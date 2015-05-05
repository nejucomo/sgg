import unittest

from spiralgalaxygame import log

from mock import patch, sentinel


class logTests (unittest.TestCase):
    @patch('logging.getLogger')
    def test_bind_logger(self, m_getLogger):

        @log.bind_logger
        def some_func(log, x):
            return (log, x)

        self.failUnless(m_getLogger.called_with('some_func'))

        expected = (m_getLogger.return_value, sentinel.x)
        actual = some_func(sentinel.x)

        self.assertEqual(expected, actual)
