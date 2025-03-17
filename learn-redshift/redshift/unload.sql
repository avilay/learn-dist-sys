unload ('select platform_id, name from platforms')
to 's3://redshift-ecomm/unload/platforms.csv' 
credentials 'aws_access_key_id=xxx;aws_secret_access_key=yyy'
null as ''
parallel off;

unload ('select plat_grp_id, platform_id from plats_grp')
to 's3://redshift-ecomm/unload/plats_grp.csv' 
credentials 'aws_access_key_id=xxx;aws_secret_access_key=yyy'
null as ''
parallel off;

unload ('select genre_id, name from genres')
to 's3://redshift-ecomm/unload/genres.csv' 
credentials 'aws_access_key_id=xxx;aws_secret_access_key=yyy'
null as ''
parallel off;

unload ('select genre_grp_id, genre_id from genres_grp')
to 's3://redshift-ecomm/unload/genres_grp.csv' 
credentials 'aws_access_key_id=xxx;aws_secret_access_key=yyy'
null as ''
parallel off;

unload ('select developer_id, name from developers')
to 's3://redshift-ecomm/unload/developers.csv' 
credentials 'aws_access_key_id=xxx;aws_secret_access_key=yyy'
null as ''
parallel off;

unload ('select dev_grp_id, developer_id from devs_grp')
to 's3://redshift-ecomm/unload/devs_grp.csv' 
credentials 'aws_access_key_id=xxx;aws_secret_access_key=yyy'
null as ''
parallel off;

unload ('select publisher_id, name from publishers')
to 's3://redshift-ecomm/unload/publishers.csv' 
credentials 'aws_access_key_id=xxx;aws_secret_access_key=yyy'
null as ''
parallel off;

unload ('select pub_grp_id, publisher_id from pubs_grp')
to 's3://redshift-ecomm/unload/pubs_grp.csv' 
credentials 'aws_access_key_id=xxx;aws_secret_access_key=yyy'
null as ''
parallel off;

unload ('select game_id, title, released_on, price, pub_grp_id, plat_grp_id, dev_grp_id, genre_grp_id from games')
to 's3://redshift-ecomm/unload/games.csv' 
credentials 'aws_access_key_id=xxx;aws_secret_access_key=yyy'
null as ''
parallel off;

unload ('select user_id, name, gender from users')
to 's3://redshift-ecomm/unload/users/users.csv' 
credentials 'aws_access_key_id=xxx;aws_secret_access_key=yyy'
null as ''
gzip;

unload ('select session_id, user_id, device, os_platform, browser, created_at from sessions')
to 's3://redshift-ecomm/unload/sessions/sessions.csv' 
credentials 'aws_access_key_id=xxx;aws_secret_access_key=yyy'
null as ''
gzip;

unload ('select visit_id, session_id, user_id, game_id, genre_grp_id, pub_grp_id, plat_grp_id, dev_grp_id, start_time, dur_secs from visits')
to 's3://redshift-ecomm/unload/visits/visits.csv' 
credentials 'aws_access_key_id=xxx;aws_secret_access_key=yyy'
null as ''
gzip;

