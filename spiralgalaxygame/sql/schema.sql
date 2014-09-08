BEGIN;

CREATE TABLE galaxy (
    uid bytea NOT NULL PRIMARY KEY,
    created timestamp WITHOUT TIME ZONE NOT NULL
);

COMMENT ON TABLE galaxy IS
'Each game takes place in a galaxy. Separate galaxies do not interact.';

COMMENT ON COLUMN galaxy.uid IS
'Every "*uid" column entry is a value of 16 high entropy bytes.';

COMMENT ON COLUMN galaxy.created IS
'Every timestamp is in UTC+0.';


CREATE TYPE body_kind AS ENUM (
    'star_white',
    'star_yellow',
    'star_red',
    'planet_blue',
    'planet_grey',
    'planet_green',
    'planet_brown',
    'black_hole',
    'dust_cloud',
    'gas_cloud'
);


CREATE TABLE body (
   uid bytea NOT NULL PRIMARY KEY,
   galaxy_uid bytea REFERENCES galaxy (uid),
   kind body_kind NOT NULL,
   geometry circle NOT NULL
);

COMMENT ON TABLE body IS
'The center and radius of stars, planets, dust clouds, and other static
environmental entities. This is written once during galaxy creation,
and not altered there-after.';

COMMENT ON COLUMN body.uid IS
'Every "*uid" column entry is a value of 16 high entropy bytes.';

COMMENT ON COLUMN body.galaxy_uid IS
'The galaxy to which this body belongs.';

COMMENT ON COLUMN body.geometry IS
'Every body is circular.';

COMMIT;
