-- This is an sql script that creates a table called users

CREATE TABLE IF NOT EXISTS users(
		id INT NOT NULL AUTO_INCREMENT,
		email CHAR(255) NOT NULL UNIQUE,
		name char(255),
		PRIMARY KEY(id)
		);

