import customtkinter as ctk
from tkinter import messagebox
import psycopg

# Configure appearance
ctk.set_appearance_mode("System")  # Options: "System", "Dark", "Light"
ctk.set_default_color_theme("blue")  # Options: "blue", "green", "dark-blue"

# Establish PostgreSQL connection
def connect_db():
    return psycopg.connect(
        host="localhost",
        dbname="Football-Club-Management-System",
        user="postgres",
        password="shiva2025"
    )

# Add Team
def add_team():
    try:
        conn = connect_db()
        cur = conn.cursor()
        cur.execute("INSERT INTO Teams (name, founded_year, city) VALUES (%s, %s, %s)",
                    (team_name.get(), team_year.get(), team_city.get()))
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Team added successfully")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Team Section
team_frame = ctk.CTkFrame(scrollable_frame)
team_frame.pack(pady=10, padx=10, fill="x")

ctk.CTkLabel(team_frame, text="Add Team", font=ctk.CTkFont(size=16, weight="bold")).pack(pady=5)

team_name = ctk.CTkEntry(team_frame, placeholder_text="Team Name")
team_name.pack(pady=5)

team_year = ctk.CTkEntry(team_frame, placeholder_text="Founded Year")
team_year.pack(pady=5)

team_city = ctk.CTkEntry(team_frame, placeholder_text="City")
team_city.pack(pady=5)

ctk.CTkButton(team_frame, text="Add Team", command=add_team).pack(pady=5)

# Add Player
def add_player():
    try:
        conn = connect_db()
        cur = conn.cursor()
        cur.execute("INSERT INTO Players (name, position, age, team_id) VALUES (%s, %s, %s, %s)",
                    (player_name.get(), player_position.get(), player_age.get(), player_team_id.get()))
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Player added successfully")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Player Section
player_frame = ctk.CTkFrame(scrollable_frame)
player_frame.pack(pady=10, padx=10, fill="x")

ctk.CTkLabel(player_frame, text="Add Player", font=ctk.CTkFont(size=16, weight="bold")).pack(pady=5)

player_name = ctk.CTkEntry(player_frame, placeholder_text="Player Name")
player_name.pack(pady=5)

player_position = ctk.CTkEntry(player_frame, placeholder_text="Position")
player_position.pack(pady=5)

player_age = ctk.CTkEntry(player_frame, placeholder_text="Age")
player_age.pack(pady=5)

player_team_id = ctk.CTkEntry(player_frame, placeholder_text="Team ID")
player_team_id.pack(pady=5)

ctk.CTkButton(player_frame, text="Add Player", command=add_player).pack(pady=5)


# Add Match
def add_match():
    try:
        conn = connect_db()
        cur = conn.cursor()
        cur.execute("INSERT INTO Matches (home_team_id, away_team_id, date, home_score, away_score) VALUES (%s, %s, %s, %s, %s)",
                    (home_team_id.get(), away_team_id.get(), match_date.get(), home_score.get(), away_score.get()))
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Match added successfully")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Match Section
match_frame = ctk.CTkFrame(scrollable_frame)
match_frame.pack(pady=10, padx=10, fill="x")

ctk.CTkLabel(match_frame, text="Add Match", font=ctk.CTkFont(size=16, weight="bold")).pack(pady=5)

home_team_id = ctk.CTkEntry(match_frame, placeholder_text="Home Team ID")
home_team_id.pack(pady=5)

away_team_id = ctk.CTkEntry(match_frame, placeholder_text="Away Team ID")
away_team_id.pack(pady=5)

match_date = ctk.CTkEntry(match_frame, placeholder_text="Match Date (YYYY-MM-DD)")
match_date.pack(pady=5)

home_score = ctk.CTkEntry(match_frame, placeholder_text="Home Score")
home_score.pack(pady=5)

away_score = ctk.CTkEntry(match_frame, placeholder_text="Away Score")
away_score.pack(pady=5)

ctk.CTkButton(match_frame, text="Add Match", command=add_match).pack(pady=5)
