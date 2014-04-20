#! /usr/bin/env python

from twisted.python.util import println
from psycopg2.extensions import AsIs
from sgg.sql.app import simple_sql_app
from sgg.async import then


DESCRIPTION = """
Create the db user and database.

This command needs to be run in the role of a PostgreSQL administrator
(which can add users and databases) prior to all other database
interaction.

On Debian the typical process (for a *dev environment*) looks like:

$ sudo apt-get install postgresql
$ sudo -u postgres sgg-db-admin-init

At this point you need to follow the instructions output by
sgg-db-admin-init to enable password authentication for other sgg
database commands.  (It's also possible to use "peer" authentication
if you make an operating system user with the same name as the --dbname
option, which defaults to "sgg_dev".)

Once that is complete, you can run the remaining tools as your normal user
(or the new sgg-specific user):

$ sgg-db-init # This only needs to be run once.
$ sgg-db-create-galaxy # Run this each time you want to create a galaxy.
$ sgg-httpd

A non-dev environment, such as a production environment, will look
the same, except we recommend you use non-defaults for --dbname, --dbuser,
and --dbpw options.
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


@simple_sql_app(DESCRIPTION)
def main(log, opts, conn, d):
    then(d, log.info, 'Creating user %r with password <redacted>.', opts.dbuser)
    then(d, conn.runOperation, 'CREATE USER %s WITH UNENCRYPTED PASSWORD %s', [AsIs(opts.dbuser), opts.dbpw])
    then(d, log.info, 'Creating databse %r owned by %r.', opts.dbname, opts.dbuser)
    then(d, conn.runOperation, 'CREATE DATABASE %s OWNER %s', [AsIs(opts.dbname), AsIs(opts.dbuser)])
    then(d, log.info, 'Finished.')
    then(d, println, PostscriptTemplate % vars(opts))


if __name__ == '__main__':
    main()
