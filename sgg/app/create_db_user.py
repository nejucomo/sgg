#! /usr/bin/env python

import sys

from twisted.internet import reactor
from txpostgres import txpostgres
from psycopg2.extensions import AsIs
from sgg.clopts import ArgumentParser
from sgg.log import bind_log


DESCRIPTION = """
%s - The Spiral Galaxy Game dbadmin

Configure postgresql database.
""" % (sys.argv[0],)


@bind_log
def main(log, args = sys.argv[1:]):
    opts = parse_args(args)

    conn = txpostgres.Connection()

    def then(d, f, *args, **kw):
        return d.addCallback(lambda _: f(*args, **kw))

    log.info('Connecting to database.')
    d = conn.connect(dbname='postgres')

    then(d, log.info, 'Creating user %r with password <redacted>.', opts.dbuser)
    then(d, conn.runOperation, 'CREATE USER %s WITH PASSWORD %s', [AsIs(opts.dbuser), opts.dbpw])
    then(d, log.info, 'Creating databse %r owned by %r.', opts.dbname, opts.dbuser)
    then(d, conn.runOperation, 'CREATE DATABASE %s OWNER %s', [AsIs(opts.dbname), AsIs(opts.dbuser)])
    then(d, log.info, 'Finished.')

    d.addErrback(lambda v: log.error('%s', v))
    d.addBoth(lambda _: reactor.stop())

    reactor.run()


def parse_args(args):
    p = ArgumentParser(DESCRIPTION)

    p.add_argument('--dbname',
                   default='sgg_dev',
                   help='database name')

    p.add_argument('--dbuser',
                   default='sgg_dev',
                   help='database user')

    p.add_argument('--dbpw',
                   default='sgg_dev',
                   help='database password')

    return p.parse_args(args)


if __name__ == '__main__':
    main()
