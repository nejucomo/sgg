#! /usr/bin/env python

import sys
import argparse
import logging

import pkg_resources

from twisted.web import server
from twisted.web.static import File
from twisted.internet import endpoints
from twisted import internet
from twisted import python


DESCRIPTION = """
%s - The Spiral Galaxy Game!
""" % (sys.argv[0],)


def main(args = sys.argv[1:]):
    parse_args(args)

    staticdir = pkg_resources.resource_filename('sgg', 'web/static')
    site = server.Site(File(staticdir))

    ep = endpoints.serverFromString(internet.reactor, 'tcp:8080')
    ep.listen(site)

    internet.reactor.run()


def parse_args(args):
    p = argparse.ArgumentParser(
        description=DESCRIPTION,
        formatter_class=argparse.RawTextHelpFormatter)

    p.add_argument('--log-level',
                   dest='loglevel',
                   default='INFO',
                   choices=['DEBUG', 'INFO', 'WARN', 'ERROR', 'CRITICAL'],
                   help='Set logging level.')

    opts = p.parse_args(args)

    logging.basicConfig(
        stream=sys.stdout,
        format='%(asctime)s %(levelname) 5s %(name)s | %(message)s',
        datefmt='%Y-%m-%dT%H:%M:%S%z',
        level=getattr(logging, opts.loglevel))

    python.log.PythonLoggingObserver().start()

    logging.getLogger('parse_args').debug('Options parsed: %r', opts)

    return opts


if __name__ == '__main__':
    main()
