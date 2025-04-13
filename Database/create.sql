g-- Table: Teams
-- Functional Dependencies: team_id → name, founded_year, city
CREATE TABLE Teams (
    team_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    founded_year INT,
    city VARCHAR(100)
);

-- Table: Players
-- Functional Dependencies:-- player_id → name, position, age, team_id

CREATE TABLE Players (
    player_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    position VARCHAR(50),
    age INT,
    team_id INT REFERENCES Teams(team_id) ON DELETE CASCADE
);

-- Table: Coaches
-- Functional Dependencies:coach_id → name, role, team_id

CREATE TABLE Coaches (
    coach_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    role VARCHAR(50),
    team_id INT REFERENCES Teams(team_id) ON DELETE CASCADE
);

-- Table: Matches
-- Functional Dependencies: match_id → home_team_id, away_team_id, date, home_score, away_score`


CREATE TABLE Matches (
    match_id SERIAL PRIMARY KEY,
    home_team_id INT REFERENCES Teams(team_id) ON DELETE CASCADE,
    away_team_id INT REFERENCES Teams(team_id) ON DELETE CASCADE,
    date DATE,
    home_score INT,
    away_score INT
);
