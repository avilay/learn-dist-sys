CREATE MASTER KEY;

CREATE DATABASE SCOPED CREDENTIAL rsmcreds
WITH
	IDENTITY = 'redshiftecomm',
	Secret = 'NlHqWLUX+R+5Fnt9E+rv9gpFaNcxcD8BKWIapTHS1h/oYZ6WMr+/cnjr2+OrC9lH8xfskVmq4ymApXFqsoymlA==';


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
