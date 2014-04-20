#! /usr/bin/env python

import sys

import pkg_resources

from twisted.internet import endpoints
from twisted import internet

from sgg.clopts import DBArgumentParser


DESCRIPTION = """
The Spiral Galaxy Game Demiurge - Creator (and Tinkerer) of Universes!
"""


def main(args = sys.argv[1:]):
    opts = DBArgumentParser.parse_args_simple(DESCRIPTION, args)

    internet.reactor.run()



if __name__ == '__main__':
    main()
