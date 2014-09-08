import sys
from functools import wraps
from twisted.internet import reactor
from sgg.clopts import DBArgumentParser
from sgg.log import bind_log
from sgg.async import then
from sgg import sql


def simple_sql_app(description, dbadmin=False):
    """A decorator for apps which simply make an SQL connection, use it, then exit."""
    def main_decorator(submain):

        @wraps(submain)
        @bind_log
        def main(log, args = sys.argv[1:]):
            opts = DBArgumentParser.parse_args_simple(description, args)

            if dbadmin:
                (dbname, dbuser, dbpw) = ('postgres', None, None)
            else:
                (dbname, dbuser, dbpw) = (opts.dbname, opts.dbuser, opts.dbpw)

            d = sql.connect(dbname, dbuser, dbpw)
            d.addCallback(submain, log, opts)
            d.addErrback(lambda v: log.error('%s', v))
            then(d, reactor.stop)

            reactor.run()

        return main

    return main_decorator
