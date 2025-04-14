# Football-Club-Management-System-

Football Club Management System - Database Application

The Football Club Management System uses a PostgreSQL database with four major tables: Teams, Players, Coaches, and Matches. The tables are meant to store football team data, players, coaches, and match data. The tables are related through foreign key associations to ensure data integrity and logical coherence.

Tables Overview:
Teams Table: Stores team data like team name, year formed, and city.

Players Table: Contains player details such as name, position, age, and the team they play for.

Coaches Table: Contains coach details such as name, role, and the team they are coaching.

Matches Table: Stores match details such as home/away teams, match date, and results.

Key Relationships:
Teams → Players: A team will have many players.

Teams → Coaches: A team might have one or several coaches.

Teams → Matches: Multiple matches can be played as home and away teams by a single team.

The relational schema provides efficient handling of the club's important entities with the assurance of data consistency across teams, players, coaches, and matches.
