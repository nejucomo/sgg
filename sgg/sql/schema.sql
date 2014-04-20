BEGIN;

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
   uid bytea not null primary key,
   universe_uid bytea not null,
   kind body_kind not null,
   geometry circle not null
);

COMMENT ON TABLE body IS
'The center and radius of stars, planets, dust clouds, and other static
environmental entities. This is written once during universe creation,
and not altered there-after.';

COMMENT ON COLUMN body.uid IS
'Every "*uid" column entry is a value of 16 high entropy bytes.';

COMMENT ON COLUMN body.universe_uid IS
'The universe to which this body belongs.';

COMMENT ON COLUMN body.geometry IS
'Every body is circular.';

COMMIT;
