
from txpostgres import txpostgres
from sgg.log import bind_log


@bind_log
def connect(log, dbname, dbuser, dbpw):
    conn = txpostgres.Connection()

    log.info('Connecting to database.')
    d = conn.connect(dbname=dbname, user=dbuser, password=dbpw)

    return (conn, d)
