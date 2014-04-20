#! /usr/bin/env python

import sys

from twisted.internet import endpoints
from twisted import internet

from sgg.clopts import DBArgumentParser
from sgg.galaxy import create_galaxy


DESCRIPTION = """
The Spiral Galaxy Game Demiurge - Creator (and Tinkerer) of Universes!
"""


def main(args = sys.argv[1:]):
    opts = DBArgumentParser.parse_args_simple(DESCRIPTION, args)

    d.addErrback(lambda v: log.error('%s', v))
    then(d, reactor.stop)

    internet.reactor.run()



if __name__ == '__main__':
    main()
