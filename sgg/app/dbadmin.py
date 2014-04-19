#! /usr/bin/env python

import sys
import subprocess

# from twisted.internet import reactor, protocol

# from txpostgres import txpostgres

from sgg.clopts import ArgumentParser
from sgg.log import bind_log


DESCRIPTION = """
%s - The Spiral Galaxy Game dbadmin

Configure postgresql database.
""" % (sys.argv[0],)


def main(args = sys.argv[1:]):
    opts = parse_args(args)

    run('createuser', opts.dbuser)
    run('createdb', '--owner', opts.dbuser, opts.dbname)


def parse_args(args):
    p = ArgumentParser(DESCRIPTION)

    p.add_argument('--dbname',
                   default='sgg-dev',
                   help='database name')

    p.add_argument('--dbuser',
                   default='sgg-dev',
                   help='database user')

    return p.parse_args(args)


@bind_log
def run(log, *args):
    log.debug('Running: %r', args)
    subprocess.check_call(argv=args)


if __name__ == '__main__':
    main()
