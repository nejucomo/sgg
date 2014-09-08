import pkg_resources
from sgg.async import then
from sgg.sql.app import simple_sql_app


DESCRIPTION = """
Create the db table schema.

The database user must already be initialized; for details run:

$ sgg-db-admin-init --help
"""


@simple_sql_app(DESCRIPTION)
def main(conn, log, opts):
    sqltransaction = pkg_resources.resource_string('sgg', 'sql/schema.sql')
    log.debug('Loaded SQL schema:\n%s', sqltransaction)

    log.info('Creating tables.')
    d = conn.runOperation(sqltransaction)
    then(d, log.info, 'Finished.')
