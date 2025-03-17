\copy users (user_id, name, gender) from '/home/avilay/data/ecomm_sample_small/users.csv' with delimiter ',' csv header;

\copy games (game_id, title, released_on, price) from '/home/avilay/data/ecomm_sample_small/games.csv' with delimiter ',' csv header;

\copy platforms (platform_id, name) from '/home/avilay/data/ecomm_sample_small/platforms.csv' with delimiter ',' csv header;

\copy games_platforms (game_platform_id, game_id, platform_id) from '/home/avilay/data/ecomm_sample_small/games_platforms.csv' with delimiter ',' csv header;

\copy genres (genre_id, name) from '/home/avilay/data/ecomm_sample_small/genres.csv' with delimiter ',' csv header;

\copy games_genres (game_genre_id, game_id, genre_id) from '/home/avilay/data/ecomm_sample_small/games_genres.csv' with delimiter ',' csv header;

\copy developers (developer_id, name) from '/home/avilay/data/ecomm_sample_small/developers.csv' with delimiter ',' csv header;

\copy games_developers (game_developer_id, game_id, developer_id) from '/home/avilay/data/ecomm_sample_small/games_developers.csv' with delimiter ',' csv header;

\copy publishers (publisher_id, name) from '/home/avilay/data/ecomm_sample_small/publishers.csv' with delimiter ',' csv header;

\copy games_publishers (game_publisher_id, game_id, publisher_id) from '/home/avilay/data/ecomm_sample_small/games_publishers.csv' with delimiter ',' csv header;

\copy orders (order_id, user_id, order_dt, amt) from '/home/avilay/data/ecomm_sample_small/orders.csv' with delimiter ',' csv header;

\copy line_items (line_item_id, order_id, game_id, qty, price) from '/home/avilay/data/ecomm_sample_small/line_items.csv' with delimiter ',' csv header;

\copy sessions (session_id, user_id, device, os_platform, browser, created_at) from '/home/avilay/data/ecomm_sample_small/sessions.csv' with delimiter ',' csv header;

\copy visits (visit_id, session_id, game_id, started_at, ended_at) from '/home/avilay/data/ecomm_sample_small/visits.csv' with delimiter ',' csv header;
