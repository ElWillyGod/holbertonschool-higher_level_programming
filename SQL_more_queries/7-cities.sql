-- create database an table con foreong key

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

CREATE TABLE hbtn_0d_usa.cities (id INT UNIQUE NOT NULL AUTO_INCREMENT,
				state_id NOT NULL,
				name VARCHAR(256) NOT NULL,
				PRIMARY KEY(id),
				FOREIGN KEY(state_id) REFERENCES states(id)
				);
