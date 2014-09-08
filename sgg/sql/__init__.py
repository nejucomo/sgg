
from txpostgres import txpostgres
from sgg.log import bind_log


@bind_log
def connect(log, dbname, dbuser, dbpw):
    log.info('Connecting to database %r as %r.', dbname, dbuser)
    conn = txpostgres.Connection()
    return conn.connect(dbname=dbname, user=dbuser, password=dbpw)
