-- script that creates the table id_not_null
CREATE TABLE IF NOT EXISTS unique_id (
	id int DEFAULT 1 UNIQUE,
	name varchar(256)
)
