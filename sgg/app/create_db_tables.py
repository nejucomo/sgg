#! /usr/bin/env python

import sys

import pkg_resources
from twisted.internet import reactor
from txpostgres import txpostgres
from sgg.clopts import ArgumentParser
from sgg.log import bind_log


DESCRIPTION = """
%s - Create the db table schema.
""" % (sys.argv[0],)


@bind_log
def main(log, args = sys.argv[1:]):
    opts = parse_args(args)

    sqltransaction = pkg_resources.resource_string('sgg', 'sql/schema.sql')
    log.debug('Loaded SQL schema:\n%s', sqltransaction)

    conn = txpostgres.Connection()

    def then(d, f, *args, **kw):
        return d.addCallback(lambda _: f(*args, **kw))

    log.info('Connecting to database.')
    d = conn.connect(dbname=opts.dbname, user=opts.dbuser, password=opts.dbpw)

    then(d, log.info, 'Creating tables.')
    then(d, conn.runOperation, sqltransaction)
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
