DO $$
DECLARE happy integer;
DECLARE frozen integer;
DECLARE cookie integer;
DECLARE gigaom integer;
DECLARE techcrunch integer;
DECLARE hacker integer;
DECLARE pydocs integer;
DECLARE quanta integer;
BEGIN
	INSERT INTO users (name, email, created_at)
	VALUES ('Happy Orange', 'happy@orange.com', current_timestamp)
	RETURNING id INTO happy;
	raise notice 'Happy Orange created with user id: %', happy;

	INSERT INTO users (name, email, created_at)
	VALUES ('Cookie Monster', 'cookie@monster.com', current_timestamp)
	RETURNING id INTO cookie;
	raise notice 'Cookie Monster created with user id: %', cookie;

	INSERT INTO users (name, email, created_at)
	VALUES ('Frozen Horizon', 'frozen@horizon.com', current_timestamp)
	RETURNING id INTO frozen;
	raise notice 'Frozen Horizon created with user id: %', frozen;


	INSERT INTO websites (title, url, crawled_at)
	VALUES ('Gigaom', 'https://gigaom.com/', '2014-09-16 21:19:23')
	RETURNING id INTO gigaom;

	INSERT INTO websites (title, url, crawled_at)
	VALUES ('Techcrunch - the latest technology news and information on startups', 'http://techcrunch.com/', '2014-09-16 21:19:23')
	RETURNING id INTO techcrunch;

	INSERT INTO websites (title, url, crawled_at)
	VALUES ('Hacker News', 'https://news.ycombinator.com/', '2014-09-16 21:19:23')
	RETURNING id INTO hacker;

	INSERT INTO websites (title, url, crawled_at)
	VALUES ('Overview -- Python 3.4.1 documentation', 'https://docs.python.org/3/', '2014-09-16 21:19:23')
	RETURNING id INTO pydocs;

	INSERT INTO websites (title, url, crawled_at)
	VALUES ('Quanta Magazine - Illuminating Science|Simons Foundation', 'http://www.simonsfoundation.org/quanta/', '2014-09-16 21:19:23')
	RETURNING id INTO quanta;


	INSERT INTO favorites (user_id, website_id, added_on, name)
	VALUES(happy, gigaom, '2014-09-16 21:19:23', 'Giga Om Biz 2.0');

	INSERT INTO favorites (user_id, website_id, added_on, name)
	VALUES(happy, techcrunch, '2014-09-16 21:19:23', 'Tech Gossip');

	INSERT INTO favorites (user_id, website_id, added_on, name)
	VALUES(happy, hacker, '2014-09-16 21:19:23', 'H@ck3rz');

	INSERT INTO favorites (user_id, website_id, added_on, name)
	VALUES(cookie, techcrunch, '2014-09-16 21:19:23', 'techy love');

	INSERT INTO favorites (user_id, website_id, added_on, name)
	VALUES(cookie, hacker, '2014-09-16 21:19:23', 'YC news');

	INSERT INTO favorites (user_id, website_id, added_on, name)
	VALUES(cookie, pydocs, '2014-09-16 21:19:23', 'python reference');

	INSERT INTO favorites (user_id, website_id, added_on, name)
	VALUES(frozen, quanta, '2014-09-16 21:19:23', 'Science news');

END $$;

