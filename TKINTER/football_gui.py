import customtkinter as ctk
from tkinter import messagebox
import psycopg
import tkinter as tk
from tkinter import ttk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

def connect_db():
    return psycopg.connect(
        host="localhost",
        dbname="Football-Club-Management-System",
        user="postgres",
        password="shiva2025"
    )

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

def view_players():
    try:
        conn = connect_db()
        cur = conn.cursor()
        cur.execute("""
            SELECT p.name, p.position, t.name 
            FROM Players p JOIN Teams t ON p.team_id = t.team_id
        """)
        rows = cur.fetchall()
        conn.close()
        for item in tree.get_children():
            tree.delete(item)
        for row in rows:
            tree.insert("", "end", values=row)
    except Exception as e:
        messagebox.showerror("Error", str(e))


root = ctk.CTk()
root.title("Football Club Management System")
root.geometry("1000x800")

scrollable_frame = ctk.CTkScrollableFrame(root, width=980, height=780)
scrollable_frame.pack(pady=10, padx=10, fill="both", expand=True)

heading = ctk.CTkLabel(scrollable_frame, text="⚽ Football Club Management", font=ctk.CTkFont(size=24, weight="bold"))
heading.pack(pady=20)

def create_labeled_entry(parent, label, variable, placeholder):
    row = ctk.CTkFrame(parent, fg_color="transparent")
    row.pack(fill="x", pady=4)
    ctk.CTkLabel(row, text=label, width=150, anchor="w").pack(side="left", padx=5)
    entry = ctk.CTkEntry(row, textvariable=variable, placeholder_text=placeholder, width=500)
    entry.pack(side="left", padx=5)
    return entry


def create_section(title, fields, button_text, button_command):
    wrapper = ctk.CTkFrame(scrollable_frame, fg_color="transparent")
    wrapper.pack(pady=10, fill="both")
    
    section = ctk.CTkFrame(wrapper, width=700, corner_radius=12)
    section.pack(pady=10)
    section.pack_propagate(False)
    
    ctk.CTkLabel(section, text=title, font=ctk.CTkFont(size=18, weight="bold")).pack(pady=10)
    
    for label, var, placeholder in fields:
        create_labeled_entry(section, label, var, placeholder)
    
    ctk.CTkButton(section, text=button_text, command=button_command).pack(pady=10)


team_name = ctk.StringVar()
team_year = ctk.StringVar()
team_city = ctk.StringVar()
create_section("🏟️ Add Team", [
    ("Team Name:", team_name, "e.g. Real Madrid"),
    ("Founded Year:", team_year, "e.g. 1902"),
    ("City:", team_city, "e.g. Madrid"),
], "Add Team", add_team)


player_name = ctk.StringVar()
player_position = ctk.StringVar()
player_age = ctk.StringVar()
player_team_id = ctk.StringVar()
create_section("👟 Add Player", [
    ("Player Name:", player_name, "e.g. Messi"),
    ("Position:", player_position, "e.g. Forward"),
    ("Age:", player_age, "e.g. 35"),
    ("Team ID:", player_team_id, "e.g. 1"),
], "Add Player", add_player)


home_team_id = ctk.StringVar()
away_team_id = ctk.StringVar()
match_date = ctk.StringVar()
home_score = ctk.StringVar()
away_score = ctk.StringVar()
create_section("🏆 Add Match", [
    ("Home Team ID:", home_team_id, "e.g. 1"),
    ("Away Team ID:", away_team_id, "e.g. 2"),
    ("Match Date:", match_date, "YYYY-MM-DD"),
    ("Home Score:", home_score, "e.g. 3"),
    ("Away Score:", away_score, "e.g. 2"),
], "Add Match", add_match)


view_wrapper = ctk.CTkFrame(scrollable_frame, fg_color="transparent")
view_wrapper.pack(pady=10, fill="both")
view_section = ctk.CTkFrame(view_wrapper, width=700, corner_radius=12)
view_section.pack(pady=10)
view_section.pack_propagate(False)
ctk.CTkLabel(view_section, text="📋 View Players with Teams", font=ctk.CTkFont(size=18, weight="bold")).pack(pady=10)
ctk.CTkButton(view_section, text="Load Players", command=view_players).pack(pady=10)


tree = ttk.Treeview(scrollable_frame, columns=("Name", "Position", "Team"), show='headings', height=10)
tree.heading("Name", text="Player Name")
tree.heading("Position", text="Position")
tree.heading("Team", text="Team")
tree.pack(pady=20, padx=20, fill="both", expand=True)

style = ttk.Style()
style.theme_use("clam")
style.configure("Treeview.Heading", font=("Arial", 12, "bold"))
style.configure("Treeview", font=("Arial", 11), rowheight=30)

root.mainloop()
