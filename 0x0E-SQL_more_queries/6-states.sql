-- script that creates the database hbtn_0d_usa and the table states
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states (
	id int AUTO_INCREMENT PRIMARY KEY,
	name varchar(256) NOT NULL
)
