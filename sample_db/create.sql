SET client_min_messages=WARNING;

-- create tables
\echo 'Creating users table'
CREATE TABLE IF NOT EXISTS users (
  id serial CONSTRAINT u_pri_key PRIMARY KEY,  
  name varchar(50),
  email varchar(50),
  created_at timestamp,
  last_activity_at timestamp
);

\echo 'Creating websites table'
CREATE TABLE IF NOT EXISTS websites (
  id serial CONSTRAINT w_pri_key PRIMARY KEY,
  title varchar(1024),
  url varchar(1024),
  crawled_at timestamp
);

\echo 'Creating favorites table'
CREATE TABLE IF NOT EXISTS favorites (
  id serial CONSTRAINT fv_pri_key PRIMARY KEY,
  added_on timestamp,
  name varchar(1024),
  user_id integer CONSTRAINT fk_fv_users REFERENCES users,
  website_id integer CONSTRAINT fk_fv_websites REFERENCES websites
);