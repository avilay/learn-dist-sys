CREATE PROCEDURE PopularGenres
AS
	SELECT g.name, COUNT(v.visit_id)
	FROM visits v, plats_grp pg, platforms p, genres_grp gg, genres g
	WHERE v.plat_grp_id = pg.plat_grp_id
	AND pg.platform_id = p.platform_id
	AND v.genre_grp_id = gg.genre_grp_id
	AND gg.genre_id = g.genre_id
	AND p.name IN ('Xbox', 'Xbox One', 'Xbox 360', 'Xbox Kinect')
	GROUP BY g.name
	ORDER BY count(v.visit_id) DESC;
GO