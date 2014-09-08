import sys
import argparse
import logging

from twisted.python import log as txpylog


class LogArgumentParser (argparse.ArgumentParser):

    @classmethod
    def parse_args_simple(cls, description, args):
        obj = cls(description)
        return obj.parse_args(args)

    def __init__(self, description):
        argparse.ArgumentParser.__init__(
            self,
            description=description,
            formatter_class=argparse.RawTextHelpFormatter)

        self.add_argument(
            '--log-level',
            dest='loglevel',
            default='INFO',
            choices=['DEBUG', 'INFO', 'WARN', 'ERROR', 'CRITICAL'],
            help='Set logging level.')

    def parse_args(self, args):
        opts = argparse.ArgumentParser.parse_args(self, args)

        logging.basicConfig(
            stream=sys.stdout,
            format='%(asctime)s %(levelname) 5s %(name)s | %(message)s',
            datefmt='%Y-%m-%dT%H:%M:%S%z',
            level=getattr(logging, opts.loglevel))

        txpylog.PythonLoggingObserver().start()

        logging.getLogger('parse_args').debug('Options parsed: %r', opts)

        return opts


class DBArgumentParser (LogArgumentParser):

    def __init__(self, description):
        LogArgumentParser.__init__(self, description)

        self.add_argument('--dbname',
                          default='sgg_dev',
                          help='database name')

        self.add_argument('--dbuser',
                          default='sgg_dev',
                          help='database user')

        self.add_argument('--dbpw',
                          default='sgg_dev',
                          help='database password')

