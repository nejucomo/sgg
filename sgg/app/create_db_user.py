#! /usr/bin/env python

import sys

from twisted.internet import reactor
from txpostgres import txpostgres
from psycopg2.extensions import AsIs
from sgg.clopts import ArgumentParser
from sgg.log import bind_log


DESCRIPTION = """
Create the db user and database.

This command needs to be run in the role of a PostgreSQL administrator
(which can add users and databases) prior to all other database
interaction.

On Debian the typical process (for a *dev environment*) looks like:

$ sudo apt-get install postgresql
$ sudo -u postgres sgg-create-db-user
$ sgg-create-db-tables
$ sgg-cron &
$ sgg-httpd &

Notice that sgg-create-db-tables does not need a special user, since
password authentication is enabled for the sgg user.

A non-dev environment, such as a production environment, will look
the same, except non-defaults for --dbname, --dbuser, and --dbpw are
recommended.
"""

PostscriptTemplate = """
Note: To access the %(dbname)r database on a standard debian postgresql
configuration, you must create an os user named %(dbuser)r or allow
password-based authentication by modifying pg_hba.conf to contain
this line:

local %(dbname)s %(dbuser)s password

Also, this line must come before any other line which would match the
local db/user access.

This must be done prior to running sgg-create-db-tables.
"""


@bind_log
def main(log, args = sys.argv[1:]):
    opts = parse_args(args)

    conn = txpostgres.Connection()

    def then(d, f, *args, **kw):
        return d.addCallback(lambda _: f(*args, **kw))

    log.info('Connecting to database.')
    d = conn.connect(dbname='postgres')

    then(d, log.info, 'Creating user %r with password <redacted>.', opts.dbuser)
    then(d, conn.runOperation, 'CREATE USER %s WITH UNENCRYPTED PASSWORD %s', [AsIs(opts.dbuser), opts.dbpw])
    then(d, log.info, 'Creating databse %r owned by %r.', opts.dbname, opts.dbuser)
    then(d, conn.runOperation, 'CREATE DATABASE %s OWNER %s', [AsIs(opts.dbname), AsIs(opts.dbuser)])
    then(d, log.info, 'Finished.')

    @d.addCallback
    def show_postscript(_):
        print PostscriptTemplate % vars(opts)

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
