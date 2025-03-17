copy users (user_id, name, gender)
from 's3://avilabs-redshift-migration/smallsample/users.csv' 
credentials 'aws_access_key_id=xxx;aws_secret_access_key=yyy'
csv
null as '';

copy platforms (platform_id, name)
from 's3://avilabs-redshift-migration/smallsample/platforms.csv' 
credentials 'aws_access_key_id=xxx;aws_secret_access_key=yyy'
csv
null as '';

copy plats_grp (plat_grp_id, platform_id)
from 's3://avilabs-redshift-migration/smallsample/plats_grp.csv'
credentials 'aws_access_key_id=xxx;aws_secret_access_key=yyy'
csv
null as '';

copy genres (genre_id, name)
from 's3://avilabs-redshift-migration/smallsample/genres.csv' 
credentials 'aws_access_key_id=xxx;aws_secret_access_key=yyy'
csv
null as '';

copy genres_grp (genre_grp_id, genre_id)
from 's3://avilabs-redshift-migration/smallsample/genres_grp.csv'
credentials 'aws_access_key_id=xxx;aws_secret_access_key=yyy'
csv
null as '';

copy developers (developer_id, name)
from 's3://avilabs-redshift-migration/smallsample/developers.csv' 
credentials 'aws_access_key_id=xxx;aws_secret_access_key=yyy'
csv
null as '';

copy devs_grp (dev_grp_id, developer_id)
from 's3://avilabs-redshift-migration/smallsample/devs_grp.csv' 
credentials 'aws_access_key_id=xxx;aws_secret_access_key=yyy'
csv
null as '';

copy publishers (publisher_id, name)
from 's3://avilabs-redshift-migration/smallsample/publishers.csv' 
credentials 'aws_access_key_id=xxx;aws_secret_access_key=yyy'
csv
null as '';

copy pubs_grp (pub_grp_id, publisher_id)
from 's3://avilabs-redshift-migration/smallsample/pubs_grp.csv' 
credentials 'aws_access_key_id=xxx;aws_secret_access_key=yyy'
csv
null as '';

copy games (game_id, title, released_on, price, pub_grp_id, plat_grp_id, dev_grp_id, genre_grp_id)
from 's3://avilabs-redshift-migration/smallsample/games.csv' 
credentials 'aws_access_key_id=xxx;aws_secret_access_key=yyy'
csv
null as '';

copy sessions (session_id, user_id, device, os_platform, browser, created_at)
from 's3://avilabs-redshift-migration/smallsample/sessions/sessions.csv' 
credentials 'aws_access_key_id=xxx;aws_secret_access_key=yyy'
csv
null as '';

copy visits (visit_id, session_id, user_id, game_id, genre_grp_id, pub_grp_id, plat_grp_id, dev_grp_id, start_time, dur_secs)
from 's3://avilabs-redshift-migration/smallsample/visits/visits.csv' 
credentials 'aws_access_key_id=xxx;aws_secret_access_key=yyy'
csv
null as '';
