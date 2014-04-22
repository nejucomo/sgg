from sgg.async import then
from sgg.sql.app import simple_sql_app
from sgg.demiurge import generate_galaxy_bodies


DESCRIPTION = """
The Spiral Galaxy Game Demiurge - Creator (and Tinkerer) of Universes!
"""


@simple_sql_app(DESCRIPTION)
def main(log, opts, conn, d):

    def interaction(cur):
        for i, body in enumerate(generate_galaxy_bodies()):
            then(d, cur.execute, 'INSERT INTO body VALUES (%s)', body)
            if i % 1000:
                then(d, log.debug, 'Inserted %d galactic bodies.', i)

    then(d, conn.runInteraction, interaction)
