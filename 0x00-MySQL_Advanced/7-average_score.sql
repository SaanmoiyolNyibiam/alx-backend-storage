-- this is a SQL script that creates a stored procedure
-- ComputeAverageScoreForUser that computes and store the
-- average score for a student. 
-- Take_Note: An average score can be a decimal

DROP PROCEDURE IF EXISTS ComputeAverageScoreForUser;

DELIMITER $$

CREATE PROCEDURE ComputeAverageScoreForUser(IN user_id INT)
	BEGIN
		-- compute students average score from corrections table
		DECLARE avg_score FLOAT;
		SELECT AVG(score) INTO avg_score
		FROM corrections
		WHERE corrections.user_id = user_id;

		-- insert students average score into users table
		UPDATE users
		SET users.average_score = avg_score
		WHERE users.id = user_id;
	END$$

DELIMITER ;

