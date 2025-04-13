
INSERT INTO Teams (name, founded_year, city) VALUES 
('Eagles FC', 1995, 'New York'),
('Tigers FC', 2000, 'Chicago');

INSERT INTO Players (name, position, age, team_id) VALUES 
('John Smith', 'Forward', 24, 1),
('Alex Ray', 'Goalkeeper', 28, 2);

INSERT INTO Coaches (name, role, team_id) VALUES 
('Michael Lee', 'Head Coach', 1),
('Sarah Green', 'Assistant Coach', 2);

INSERT INTO Matches (home_team_id, away_team_id, date, home_score, away_score) VALUES 
(1, 2, '2025-04-10', 3, 1);
