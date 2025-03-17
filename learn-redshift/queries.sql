SELECT COUNT(visit_id) AS num_visits FROM visits;
SELECT COUNT(session_id) AS num_sessions FROM sessions;
SELECT COUNT(game_id) AS num_games FROM games;
SELECT COUNT(pub_grp_id) AS num_pubs_grp FROM pubs_grp;
SELECT COUNT(publisher_id) AS num_publishers FROM publishers;
SELECT COUNT(dev_grp_id) AS num_devs_grp FROM devs_grp;
SELECT COUNT(developer_id) AS num_developers FROM developers;
SELECT COUNT(genre_grp_id) AS num_genres_grp FROM genres_grp;
SELECT COUNT(genre_id) AS num_genres FROM genres;
SELECT COUNT(plat_grp_id) AS num_plats_grp FROM plats_grp;
SELECT COUNT(platform_id) AS num_platforms FROM platforms;
SELECT COUNT(user_id) AS num_users FROM users;

SELECT s.os_platform, COUNT(v.visit_id)
FROM visits v, sessions s
WHERE v.session_id = s.session_id
GROUP BY s.os_platform
ORDER BY COUNT(v.visit_id) DESC;

SELECT g.name, COUNT(v.visit_id)
FROM visits v, plats_grp pg, platforms p, genres_grp gg, genres g
WHERE v.plat_grp_id = pg.plat_grp_id
AND pg.platform_id = p.platform_id
AND v.genre_grp_id = gg.genre_grp_id
AND gg.genre_id = g.genre_id
AND p.name IN ('Xbox', 'Xbox One', 'Xbox 360', 'Xbox Kinect')
GROUP BY g.name
ORDER BY count(v.visit_id) DESC;

