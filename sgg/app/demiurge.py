#! /usr/bin/env python

import sys

import pkg_resources

from twisted.internet import endpoints
from twisted import internet

from sgg.clopts import ArgumentParser


DESCRIPTION = """
The Spiral Galaxy Game Demiurge - Creator (and Tinkerer) of Universes!
"""


def main(args = sys.argv[1:]):
    parse_args(args)

    internet.reactor.run()


def parse_args(args):
    p = ArgumentParser(DESCRIPTION)
    return p.parse_args(args)


if __name__ == '__main__':
    main()
