==================
Spiral Galaxy Game
==================

Spiral Galaxy Game - an open source semi-massively multiplayer turn
based space strategy game!  (-with a rather generic title.)

Status
======

This codebase is currently exploratory as I'm learning a lot about
PostgresQL, twisted web apps, and html5.

Quick Start
===========

This assumes a debian-like system::

    $ git checkout https://github.com/nejucomo/sgg
    $ cd ./sgg
    $ T="$HOME/virtualenvs/sgg-dev"
    $ mkdir -p "$T"
    $ virtualenv "$T"
    $ source "$T/bin/activate"
    $ ./setup.py develop
    $ sudo apt-get install postgresql{,-doc,-client}
    $ sudo -u postgres $(which sgg-create-db-user)

If all has gone well ``sgg-create-db-user`` should have given instructions
for how to edit ``pg_hba.conf``, so follow them::

    $ sudo vim /etc/postgresql/9.3/main/pg_hba.conf
    $ sudo /etc/init.d/postgresql reload

This step is not yet implemented::

    $ sgg-demiurge # Create a galaxy.
