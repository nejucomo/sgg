#! /usr/bin/env python

import sys

import pkg_resources
from twisted.internet import reactor
from txpostgres import txpostgres
from sgg.clopts import DBArgumentParser
from sgg.log import bind_log
from sgg.async import then


DESCRIPTION = """
Create the db table schema.

The database user must already be initialized; for details run:

$ sgg-db-admin-init --help
"""


@bind_log
def main(log, args = sys.argv[1:]):
    opts = DBArgumentParser.parse_args_simple(DESCRIPTION, args)

    sqltransaction = pkg_resources.resource_string('sgg', 'sql/schema.sql')
    log.debug('Loaded SQL schema:\n%s', sqltransaction)

    conn = txpostgres.Connection()

    log.info('Connecting to database.')
    d = conn.connect(dbname=opts.dbname, user=opts.dbuser, password=opts.dbpw)

    then(d, log.info, 'Creating tables.')
    then(d, conn.runOperation, sqltransaction)
    then(d, log.info, 'Finished.')

    d.addErrback(lambda v: log.error('%s', v))
    then(d, reactor.stop)

    reactor.run()



if __name__ == '__main__':
    main()
