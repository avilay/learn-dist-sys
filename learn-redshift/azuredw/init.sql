CREATE MASTER KEY;

CREATE DATABASE SCOPED CREDENTIAL rsmcreds
WITH
	IDENTITY = 'redshiftecomm',
	Secret = 'xxx';


CREATE EXTERNAL DATA SOURCE azure_storage
WITH (
    TYPE = HADOOP,   
	LOCATION ='wasbs://ecomm@redshiftecomm.blob.core.windows.net',   
	CREDENTIAL = rsmcreds
);


CREATE EXTERNAL FILE FORMAT pipe_file_format
WITH (
    FORMAT_TYPE = DELIMITEDTEXT,   
	FORMAT_OPTIONS (
		FIELD_TERMINATOR ='|', 
		USE_TYPE_DEFAULT = FALSE
	)
);
