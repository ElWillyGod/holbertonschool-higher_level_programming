-- create database and table con primary key

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

CREATE TABLE IF NOT EXISTS hbtn_0d_usa.states (id int UNIQUE NOT NULL AUTO_INCREMENT,
	name VARCHAR(256),
	PRIMARY KEY(id));
