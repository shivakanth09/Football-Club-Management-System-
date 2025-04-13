
-- Create
INSERT INTO Players (name, position, age, team_id) VALUES ('David Miller', 'Midfielder', 22, 1);

-- Read (Join Query)
SELECT p.name AS Player, p.position, t.name AS Team 
FROM Players p 
JOIN Teams t ON p.team_id = t.team_id;

-- Update
UPDATE Matches SET home_score = 4 WHERE match_id = 1;

-- Delete
DELETE FROM Coaches WHERE coach_id = 2;


