import sys
import argparse
import logging

from twisted.python import log as txpylog


class ArgumentParser (argparse.ArgumentParser):

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
