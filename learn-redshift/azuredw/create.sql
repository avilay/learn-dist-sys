-- create users table
CREATE EXTERNAL TABLE [ext_users] (
     [user_id] int NOT NULL,
	 [name] varchar(128),
	 [gender] varchar(6)
)
WITH (
    LOCATION = '/users/',
	DATA_SOURCE = azure_storage,
	FILE_FORMAT = pipe_file_format
);

CREATE TABLE [dbo].[users]
WITH (   
    CLUSTERED COLUMNSTORE INDEX,
	DISTRIBUTION = HASH([user_id])
)
AS SELECT * FROM [ext_users];

CREATE STATISTICS stats_user_user_id on [users] (user_id);
CREATE STATISTICS stats_user_name on [users] (name);
CREATE STATISTICS stats_user_gender on [users] (gender);

GO

-- create platforms table
CREATE EXTERNAL TABLE [ext_platforms] (
	[platform_id] INTEGER NOT NULL,
	[name] VARCHAR(1024)
)
WITH (
    LOCATION = '/platforms.csv000',
	DATA_SOURCE = azure_storage,
	FILE_FORMAT = pipe_file_format
);

CREATE TABLE [dbo].[platforms]
WITH (
	CLUSTERED COLUMNSTORE INDEX,
	DISTRIBUTION = ROUND_ROBIN
)
AS SELECT * FROM [ext_platforms];

CREATE STATISTICS stats_platforms_platform_id on [platforms] (platform_id);
CREATE STATISTICS stats_platforms_name on [platforms] (name);

GO

-- create plats_grp table
CREATE EXTERNAL TABLE [ext_plats_grp] (
	[plat_grp_id] INTEGER NOT NULL,
	[platform_id] INTEGER NOT NULL
)
WITH (
	LOCATION = '/plats_grp.csv000',
	DATA_SOURCE = azure_storage,
	FILE_FORMAT = pipe_file_format
);

CREATE TABLE [dbo].[plats_grp]
WITH (
	CLUSTERED COLUMNSTORE INDEX,
	DISTRIBUTION = ROUND_ROBIN
)
AS SELECT * FROM [ext_plats_grp];

CREATE STATISTICS stats_plats_grp_plat_grp_id on [plats_grp] (plat_grp_id);
CREATE STATISTICS stats_plats_grp_platform_id on [plats_grp] (platform_id);

GO

-- create genres table
CREATE EXTERNAL TABLE [ext_genres] (
	[genre_id] INTEGER NOT NULL,
	[name] VARCHAR(256)
)
WITH (
	LOCATION = '/genres.csv000',
	DATA_SOURCE = azure_storage,
	FILE_FORMAT = pipe_file_format
);

CREATE TABLE [dbo].[genres]
WITH (
	CLUSTERED COLUMNSTORE INDEX,
	DISTRIBUTION = ROUND_ROBIN
)
AS SELECT * FROM [ext_genres];

CREATE STATISTICS stats_genres_genre_id on [genres] (genre_id);
CREATE STATISTICS stats_genres_name on [genres] (name);

GO

-- create genres_grp table
CREATE EXTERNAL TABLE [ext_genres_grp] (
	[genre_grp_id] INTEGER,
	[genre_id] INTEGER NOT NULL
)
WITH (
	LOCATION = '/genres_grp.csv000',
	DATA_SOURCE = azure_storage,
	FILE_FORMAT = pipe_file_format
);

CREATE TABLE [dbo].[genres_grp]
WITH (
	CLUSTERED COLUMNSTORE INDEX,
	DISTRIBUTION = ROUND_ROBIN
)
AS SELECT * FROM [ext_genres_grp];

CREATE STATISTICS stats_genres_grp_genre_grp_id on [genres_grp] (genre_grp_id);
CREATE STATISTICS stats_genres_grp_genre_id on [genres_grp] (genre_id);

GO

-- create developers table
CREATE EXTERNAL TABLE [ext_developers] (
	[developer_id] INTEGER NOT NULL,
	[name] VARCHAR(1024)
)
WITH (
	LOCATION = '/developers.csv000',
	DATA_SOURCE = azure_storage,
	FILE_FORMAT = pipe_file_format
);

CREATE TABLE [dbo].[developers]
WITH (
	CLUSTERED COLUMNSTORE INDEX,
	DISTRIBUTION = ROUND_ROBIN
)
AS SELECT * FROM [ext_developers];

CREATE STATISTICS stats_developers_developer_id on [developers] (developer_id);
CREATE STATISTICS stats_developers_name on [developers] (name);

GO

-- create devs_grp table
CREATE EXTERNAL TABLE [ext_devs_grp] (
	[dev_grp_id] INTEGER NOT NULL,
	[developer_id] INTEGER NOT NULL	
)
WITH (
	LOCATION = '/devs_grp.csv000',
	DATA_SOURCE = azure_storage,
	FILE_FORMAT = pipe_file_format
);

CREATE TABLE [dbo].[devs_grp]
WITH (
	CLUSTERED COLUMNSTORE INDEX,
	DISTRIBUTION = ROUND_ROBIN
)
AS SELECT * FROM [ext_devs_grp];

CREATE STATISTICS stats_devs_grp_dev_grp_id on [devs_grp] (dev_grp_id);
CREATE STATISTICS stats_devs_grp_developer_id on [devs_grp] (developer_id);

GO

-- create publishers table
CREATE EXTERNAL TABLE [ext_publishers] (
	[publisher_id] INTEGER NOT NULL,
	[name] VARCHAR(1024)	
)
WITH (
	LOCATION = '/publishers.csv000',
	DATA_SOURCE = azure_storage,
	FILE_FORMAT = pipe_file_format
);

CREATE TABLE [dbo].[publishers]
WITH (
	CLUSTERED COLUMNSTORE INDEX,
	DISTRIBUTION = ROUND_ROBIN
)
AS SELECT * FROM [ext_publishers];

CREATE STATISTICS stats_publishers_publisher_id on [publishers] (publisher_id);
CREATE STATISTICS stats_publishers_name on [publishers] (name);

GO

-- create pubs_grp table
CREATE EXTERNAL TABLE [ext_pubs_grp] (
	[pub_grp_id] INTEGER NOT NULL,
	[publisher_id] INTEGER NOT NULL	
)
WITH (
	LOCATION = '/pubs_grp.csv000',
	DATA_SOURCE = azure_storage,
	FILE_FORMAT = pipe_file_format
);

CREATE TABLE [dbo].[pubs_grp]
WITH (
	CLUSTERED COLUMNSTORE INDEX,
	DISTRIBUTION = ROUND_ROBIN
)
AS SELECT * FROM [ext_pubs_grp];

CREATE STATISTICS stats_pubs_grp_pub_grp_id on [pubs_grp] (pub_grp_id);
CREATE STATISTICS stats_pubs_grp_publisher_id on [pubs_grp] (publisher_id);

GO

-- create games table
CREATE EXTERNAL TABLE [ext_games] (
	[game_id] INTEGER NOT NULL,
	[title] VARCHAR(1024) NOT NULL,
	[released_on] DATE,
	[price] DECIMAL(6, 2) NOT NULL,
    [pub_grp_id] INTEGER,
    [plat_grp_id] INTEGER,
    [dev_grp_id]  INTEGER,
    [genre_grp_id] INTEGER	
)
WITH (
	LOCATION = '/games.csv000',
	DATA_SOURCE = azure_storage,
	FILE_FORMAT = pipe_file_format
);

CREATE TABLE [dbo].[games]
WITH (
	CLUSTERED COLUMNSTORE INDEX,
	DISTRIBUTION = ROUND_ROBIN
)
AS SELECT * FROM [ext_games];

CREATE STATISTICS stats_games_game_id on [games] (game_id);
CREATE STATISTICS stats_games_title on [games] (title);
CREATE STATISTICS stats_games_released_on on [games] (released_on);
CREATE STATISTICS stats_games_price on [games] (price);
CREATE STATISTICS stats_games_pub_grp_id on [games] (pub_grp_id);
CREATE STATISTICS stats_games_plat_grp_id on [games] (plat_grp_id);
CREATE STATISTICS stats_dev_grp_id on [games] (dev_grp_id);
CREATE STATISTICS stats_genre_grp_id on [games] (genre_grp_id);

GO
-- create sessions table
CREATE EXTERNAL TABLE [ext_sessions] (
	[session_id] INTEGER,
	[user_id] INTEGER,
	[device] VARCHAR(32),
	[os_platform] VARCHAR(32),
	[browser] VARCHAR(32),
	[created_at] DATETIME	
)
WITH (
	LOCATION = '/sessions/',
	DATA_SOURCE = azure_storage,
	FILE_FORMAT = pipe_file_format
);

CREATE TABLE [dbo].[sessions]
WITH (
	CLUSTERED COLUMNSTORE INDEX,
	DISTRIBUTION = HASH([session_id]),
	PARTITION (
		[os_platform] RANGE RIGHT FOR VALUES
        ('android', 'linux', 'macos', 'ios', 'windows')
    )
)
AS SELECT * FROM [ext_sessions];

CREATE STATISTICS stats_sessions_session_id on [sessions] (session_id);
CREATE STATISTICS stats_sessions_user_id on [sessions] (user_id);
CREATE STATISTICS stats_sessions_device on [sessions] (device);
CREATE STATISTICS stats_sessions_os_platform on [sessions] (os_platform);
CREATE STATISTICS stats_sessions_browser on [sessions] (browser);
CREATE STATISTICS stats_created_at on [sessions] (created_at);

GO

-- create visits table
CREATE EXTERNAL TABLE [ext_visits] (
	[visit_id] INTEGER NOT NULL,
	[session_id] INTEGER NOT NULL,
	[user_id] INTEGER NOT NULL,
	[game_id] INTEGER NOT NULL,
	[genre_grp_id] INTEGER,
	[pub_grp_id] INTEGER,
	[plat_grp_id] INTEGER,
	[dev_grp_id]  INTEGER,
	[start_time] DATETIME,
	[dur_secs] INTEGER	
)
WITH (
	LOCATION = '/visits/',
	DATA_SOURCE = azure_storage,
	FILE_FORMAT = pipe_file_format
);

CREATE TABLE [dbo].[visits]
WITH (
	CLUSTERED COLUMNSTORE INDEX,
	DISTRIBUTION = HASH([session_id]),
	PARTITION (
		[start_time] RANGE RIGHT FOR VALUES
		('2015-03-01', '2015-04-01', '2015-05-01', '2015-06-01')
	)
)
AS SELECT * FROM [ext_visits];

CREATE STATISTICS stats_visits_visit_id on [visits] (visit_id);
CREATE STATISTICS stats_visits_session_id on [visits] (session_id);
CREATE STATISTICS stats_visits_user_id on [visits] (user_id);
CREATE STATISTICS stats_visits_game_id on [visits] (game_id);
CREATE STATISTICS stats_visits_genre_grp_id on [visits] (genre_grp_id);
CREATE STATISTICS stats_visits_pub_grp_id on [visits] (pub_grp_id);
CREATE STATISTICS stats_visits_plat_grp_id on [visits] (plat_grp_id);
CREATE STATISTICS stats_visits_dev_grp_id on [visits] (dev_grp_id);
CREATE STATISTICS stats_visits_start_time on [visits] (start_time);
CREATE STATISTICS stats_visits_dur_secs on [visits] (dur_secs);

GO