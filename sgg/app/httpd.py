#! /usr/bin/env python

import sys

import pkg_resources

from twisted.web import server
from twisted.web.static import File
from twisted.internet import endpoints
from twisted import internet

from sgg.clopts import ArgumentParser


DESCRIPTION = """
The Spiral Galaxy Game web server.
"""


def main(args = sys.argv[1:]):
    parse_args(args)

    staticdir = pkg_resources.resource_filename('sgg', 'web/static')
    site = server.Site(File(staticdir))

    ep = endpoints.serverFromString(internet.reactor, 'tcp:8080')
    ep.listen(site)

    internet.reactor.run()


def parse_args(args):
    p = ArgumentParser(DESCRIPTION)
    return p.parse_args(args)


if __name__ == '__main__':
    main()
