============
Architecture
============

User Flow
=========

Users interact with a website to create/delete/configure their accounts,
examine open games, join games, make moves in games, and see the history
of past games.

Games are periodically created with different parameters and have three
phases: open, running, and complete.

Users can choose to join open games (thus becoming players), which
eventually transition into "running" in which case new players cannot
join.

Games are running for a set number of turns, and then they complete.

Turns are "simultaneous move" and regularly scheduled, depending on game
parameters. For instance a common format will be one-day turns, 30
turn games.

Since games have a natural time limit, the software distribution will be
"multi-versioned": a user may be a player in two or more games which
are running different versions of the game application software.

Components
==========

Database
~~~~~~~~

The architecture is a "shared nothing" web application, so all shared
state between http requests should go through the database, and not be
shared in application process memory.

Decoupled Tables
----------------

The database has separate tables for each version of each of the
`Areas`_, and may have even futher separate tables for separate
games or other natural application compartmentalization.

``httpd``
~~~~~~~~~

The ``httpd`` component is a horizontally scalable, shared-nothing web
application which interacts with the database(s).

Shared-Nothing
--------------

The web application server is shared-nothing, so two `HTTP` requests
should share no dynamic state within the application process.  Instead,
all shared state should go through the database.  This is both to enforce
a simplifying convention in the code architecture and runtime, as well
as to promote horizontal scalability.

URL Format
----------

The game URLs always begin with::

  https://«DOMAIN»/«AREA»/«VERSION»/

The `Areas`_ and version used in `Multi-Versioning`_ are described
below.

Frontend
--------

The frontend is an `HTML5` interface with a `rigidly separation between
static declarations and dynamic API`, aka `Rigidly Separate` API.

This means there are no server side template generations.  There are
only static files + a programmatic web API.  All html and javascript is
served as it lives on the webapp's disk.

The static files are tightly coupled to the API and entire application,
and as such they are bundled with the software and released with the
software.  Static files should never be altered outside of the standard
package distribution mechanism.

Multi-Versioning
----------------

The ``httpd`` process uses `multi-versioning` where the versions
represent changes to db scheme or changes to the web API (including
static files). This is distinct from the software revision, which may
change without changes to schema or web API, in order to fix bugs or
develop new features.

Different `Areas`_ have decoupled versioning (as well as `Decoupled
Tables`_.

Areas
-----

.. note:: This abstraction really needs a better name.

The application is divided into separate `areas`, of which there are
currently two `area-kinds`:

* `Lobby` areas, and
* `Play` areas.

The combination of `area-kind` and `version` determines an `area-spec`,
which implies an ideally fixed web API and database schema [#]_.

.. [#] When we say "schema" here we mean the whole set of database
    connections, their associated static set of table names, and the
    statically defined schema for each of those tables.

The `version` is an interface abstraction for the web API and db schema,
and is distinct from software `revision`.  Multiple software revisions
may implement the same `area-spec`.  For each `area-spec` there may be
multiple `revisions` of software for that spec, and for each revision
there may be multiple software/process-cluster `instances`.

The Lobby
.........

The `Lobby` area is where users interact with the website to:

* Create new accounts.
* Authenticate existing accounts.
* Interact with open games:

    + By listing them, and
    + By joining them.

* Interact with their running games:

    + By seeing a list of games they are playing in (along with which have un-made moves).
    + Browsing to the `Play Area` for one of their running games.

* See details about past games:
* (Maybe?) See details about other running games.

