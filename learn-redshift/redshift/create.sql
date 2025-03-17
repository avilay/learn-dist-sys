CREATE TABLE users (
	user_id INTEGER NOT NULL CONSTRAINT pk_users PRIMARY KEY SORTKEY DISTKEY,
	name VARCHAR(128),
	gender VARCHAR(6)
)
DISTSTYLE KEY;

CREATE TABLE platforms (
	platform_id INTEGER NOT NULL CONSTRAINT pk_platforms PRIMARY KEY,
	name VARCHAR(1024) SORTKEY
)
DISTSTYLE ALL;

CREATE TABLE plats_grp (
  plat_grp_id INTEGER NOT NULL CONSTRAINT pk_plats_grp PRIMARY KEY,
  platform_id INTEGER NOT NULL CONSTRAINT fk_plats_grp_platforms REFERENCES platforms 
)
DISTSTYLE ALL;

CREATE TABLE genres (
	genre_id INTEGER NOT NULL CONSTRAINT pk_genres PRIMARY KEY SORTKEY,
	name VARCHAR(256)
)
DISTSTYLE ALL;

CREATE TABLE genres_grp (
  genre_grp_id INTEGER NOT NULL CONSTRAINT pk_genres_grp PRIMARY KEY,
  genre_id INTEGER NOT NULL CONSTRAINT fk_genres_grp_genres REFERENCES genres SORTKEY
)
DISTSTYLE ALL;

CREATE TABLE developers (
	developer_id INTEGER NOT NULL CONSTRAINT pk_developers PRIMARY KEY SORTKEY,
	name VARCHAR(1024)
)
DISTSTYLE ALL;

CREATE TABLE devs_grp (
  dev_grp_id INTEGER NOT NULL CONSTRAINT pk_devs_grp PRIMARY KEY,
  developer_id INTEGER NOT NULL CONSTRAINT fk_devs_grp_developers REFERENCES developers SORTKEY
)
DISTSTYLE ALL;

CREATE TABLE publishers (
	publisher_id INTEGER NOT NULL CONSTRAINT pk_publishers PRIMARY KEY SORTKEY,
	name VARCHAR(1024)
)
DISTSTYLE ALL;

CREATE TABLE pubs_grp (
  pub_grp_id INTEGER NOT NULL CONSTRAINT pk_pubs_grp PRIMARY KEY,
  publisher_id INTEGER NOT NULL CONSTRAINT fk_pubs_grp_publishers REFERENCES publishers SORTKEY
)
DISTSTYLE ALL;


CREATE TABLE games (
	game_id INTEGER NOT NULL CONSTRAINT pk_games PRIMARY KEY SORTKEY,
	title VARCHAR(1024) NOT NULL,
	released_on DATE,
	price DECIMAL(6, 2) NOT NULL,
  pub_grp_id INTEGER CONSTRAINT fk_games_pubs_grp REFERENCES pubs_grp,
  plat_grp_id INTEGER CONSTRAINT fk_games_plats_grp REFERENCES plats_grp,
  dev_grp_id  INTEGER CONSTRAINT fk_games_devs_grp REFERENCES devs_grp,
  genre_grp_id INTEGER CONSTRAINT fk_games_genres_grp REFERENCES genres_grp
)
DISTSTYLE EVEN;

CREATE TABLE sessions (
	session_id INTEGER NOT NULL CONSTRAINT pk_sessions PRIMARY KEY DISTKEY,
	user_id INTEGER NOT NULL CONSTRAINT fk_sessions_users REFERENCES users,
	device VARCHAR(32),
	os_platform VARCHAR(32) SORTKEY,
	browser VARCHAR(32),
	created_at TIMESTAMP
)
DISTSTYLE KEY;

CREATE TABLE visits (
	visit_id INTEGER NOT NULL CONSTRAINT pk_visits PRIMARY KEY,
	session_id INTEGER NOT NULL CONSTRAINT fk_visits_sessions REFERENCES sessions DISTKEY SORTKEY,
	user_id INTEGER NOT NULL CONSTRAINT fk_visits_users REFERENCES users,
	game_id INTEGER NOT NULL CONSTRAINT fk_visits_games REFERENCES games,
	genre_grp_id INTEGER CONSTRAINT fk_visits_genres_grp REFERENCES genres_grp,
	pub_grp_id INTEGER CONSTRAINT fk_visits_pubs_grp REFERENCES pubs_grp,
	plat_grp_id INTEGER CONSTRAINT fk_visits_plats_grp REFERENCES plats_grp,
	dev_grp_id  INTEGER CONSTRAINT fk_visits_devs_grp REFERENCES devs_grp,
	start_time TIMESTAMP,
	dur_secs INTEGER
)
DISTSTYLE KEY;
