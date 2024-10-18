-- This is an SQL script that creates a stored procedure AddBonus
-- that adds a new correction for a student.

DROP PROCEDURE IF EXISTS AddBonus;

DELIMITER $$

CREATE PROCEDURE AddBonus(
		IN user_id INT,
		IN project_name VARCHAR(255),
		IN score FLOAT
		)
	BEGIN
		-- get project_id based on project_name
		DECLARE project_id INT;
		SELECT id INTO project_id FROM projects
		WHERE name = project_name;

		-- create project if it does not exist
		IF project_id IS NULL THEN
			INSERT INTO projects(name) VALUES(project_name);
		    	SET project_id = LAST_INSERT_ID();
		END IF;

		-- update project in corrections tables
		INSERT INTO corrections(user_id, project_id, score) VALUES(user_id, project_id, score);
	END$$

DELIMITER ;

