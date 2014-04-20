#! /usr/bin/env python

from sgg.sql.app import simple_sql_app


DESCRIPTION = """
The Spiral Galaxy Game Demiurge - Creator (and Tinkerer) of Universes!
"""


@simple_sql_app(DESCRIPTION)
def main(log, opts, conn, d):
    return


if __name__ == '__main__':
    main()
