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

def update_team():
    try:
        conn = connect_db()
        cur = conn.cursor()
        cur.execute("UPDATE Teams SET name=%s, founded_year=%s, city=%s WHERE team_id=%s",
                    (team_name.get(), team_year.get(), team_city.get(), team_id.get()))
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Team updated successfully")
    except Exception as e:
        messagebox.showerror("Error", str(e))


def delete_team():
    try:
        conn = connect_db()
        cur = conn.cursor()
        cur.execute("DELETE FROM Teams WHERE team_id=%s", (team_id.get(),))
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Team deleted successfully")
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

def add_coach():
    try:
        conn = connect_db()
        cur = conn.cursor()
        cur.execute("INSERT INTO Coaches (name, role, team_id) VALUES (%s, %s, %s)",
                    (coach_name.get(), coach_role.get(), coach_team_id.get()))
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Coach added successfully")
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

def view_coaches():
    try:
        conn = connect_db()
        cur = conn.cursor()
        cur.execute("""
            SELECT c.name, c.role, t.name
            FROM Coaches c
            JOIN Teams t ON c.team_id = t.team_id
        """)
        rows = cur.fetchall()
        conn.close()
        
        for item in tree.get_children():
            tree.delete(item)
        
        for row in rows:
            tree.insert("", "end", values=row)
    except Exception as e:
        messagebox.showerror("Error", str(e))


def update_coach():
    try:
        conn = connect_db()
        cur = conn.cursor()
        cur.execute("UPDATE Coaches SET name=%s, role=%s, team_id=%s WHERE coach_id=%s",
                    (coach_name.get(), coach_role.get(), coach_team_id.get(), coach_id.get()))
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Coach updated successfully")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def delete_coach():
    try:
        conn = connect_db()
        cur = conn.cursor()
        cur.execute("DELETE FROM Coaches WHERE coach_id=%s", (coach_id.get(),))
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Coach deleted successfully")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def update_player():
    try:
        conn = connect_db()
        cur = conn.cursor()
        cur.execute("UPDATE Players SET name=%s, position=%s, age=%s, team_id=%s WHERE player_id=%s",
                    (player_name.get(), player_position.get(), player_age.get(), player_team_id.get(), player_id.get()))
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Player updated successfully")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def delete_player():
    try:
        conn = connect_db()
        cur = conn.cursor()
        cur.execute("DELETE FROM Players WHERE player_id=%s", (player_id.get(),))
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Player deleted successfully")
    except Exception as e:
        messagebox.showerror("Error", str(e))


def update_match():
    try:
        conn = connect_db()
        cur = conn.cursor()
        cur.execute("""
            UPDATE Matches
            SET home_team_id=%s, away_team_id=%s, date=%s, home_score=%s, away_score=%s
            WHERE match_id=%s
        """, (home_team_id.get(), away_team_id.get(), match_date.get(), home_score.get(), away_score.get(), match_id.get()))
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Match updated successfully")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def delete_match():
    try:
        conn = connect_db()
        cur = conn.cursor()
        cur.execute("DELETE FROM Matches WHERE match_id=%s", (match_id.get(),))
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Match deleted successfully")
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
    row.pack(pady=4)

    label_widget = ctk.CTkLabel(row, text=label, width=150, anchor="e")
    label_widget.grid(row=0, column=0, padx=10, pady=5)

    entry = ctk.CTkEntry(row, textvariable=variable, placeholder_text=placeholder, width=300)
    entry.grid(row=0, column=1, padx=10, pady=5)

    # Center the entire row
    row.grid_columnconfigure(0, weight=1)
    row.grid_columnconfigure(1, weight=1)

    return entry


def create_section(title, fields, buttons):
    wrapper = ctk.CTkFrame(scrollable_frame, fg_color="transparent")
    wrapper.pack(pady=10, fill="both", expand=True)

    section = ctk.CTkFrame(wrapper, width=700, height=420, corner_radius=12)
    section.pack(pady=10)
    section.pack_propagate(False)

    ctk.CTkLabel(section, text=title, font=ctk.CTkFont(size=18, weight="bold")).pack(pady=10)

    center_frame = ctk.CTkFrame(section, fg_color="transparent")
    center_frame.pack()

    for label, var, placeholder in fields:
        create_labeled_entry(center_frame, label, var, placeholder)

    # Button row
    btn_row = ctk.CTkFrame(section, fg_color="transparent")
    btn_row.pack(pady=10)
    for (text, command) in buttons:
        ctk.CTkButton(btn_row, text=text, command=command).pack(side="left", padx=5)


team_name = ctk.StringVar()
team_year = ctk.StringVar()
team_city = ctk.StringVar()
team_id = ctk.StringVar()  
# Custom section for Add/Update/Delete Team
team_section = ctk.CTkFrame(scrollable_frame, fg_color="transparent")
team_section.pack(pady=10, fill="both", expand=True)

inner_frame = ctk.CTkFrame(team_section, width=700, height=300, corner_radius=12)
inner_frame.pack(pady=10, fill="both", expand=True)
inner_frame.pack_propagate(False)

ctk.CTkLabel(inner_frame, text="🏟️ Add/Manage Team", font=ctk.CTkFont(size=18, weight="bold")).pack(pady=10)

for label, var, placeholder in [
    ("Team ID:", team_id, "e.g. 1"),
    ("Team Name:", team_name, "e.g. Real Madrid"),
    ("Founded Year:", team_year, "e.g. 1902"),
    ("City:", team_city, "e.g. Madrid"),
]:
    create_labeled_entry(inner_frame, label, var, placeholder)

# Buttons in a horizontal layout
btn_frame = ctk.CTkFrame(inner_frame, fg_color="transparent")
btn_frame.pack(pady=10)
ctk.CTkButton(btn_frame, text="Add Team", command=add_team).pack(side="left", padx=10)
ctk.CTkButton(btn_frame, text="Update Team", command=update_team).pack(side="left", padx=10)
ctk.CTkButton(btn_frame, text="Delete Team", command=delete_team).pack(side="left", padx=10)



coach_name = ctk.StringVar()
coach_role = ctk.StringVar()
coach_team_id = ctk.StringVar()
coach_id = ctk.StringVar()
player_id = ctk.StringVar()



create_section("🧑‍🏫 Coach Details", [
    ("Coach ID:", coach_id, "e.g. 1"),
    ("Coach Name:", coach_name, "e.g. Zinedine Zidane"),
    ("Role:", coach_role, "e.g. Head Coach"),
    ("Team ID:", coach_team_id, "e.g. 1"),
], [
    ("Add Coach", add_coach),
    ("Update Coach", update_coach),
    ("Delete Coach", delete_coach)
])


player_name = ctk.StringVar()
player_position = ctk.StringVar()
player_age = ctk.StringVar()
player_team_id = ctk.StringVar()
player_id = ctk.StringVar()

create_section("👟 Player Details", [
    ("Player ID:", player_id, "e.g. 1"),
    ("Player Name:", player_name, "e.g. Messi"),
    ("Position:", player_position, "e.g. Forward"),
    ("Age:", player_age, "e.g. 35"),
    ("Team ID:", player_team_id, "e.g. 1"),
], [
    ("Add Player", add_player),
    ("Update Player", update_player),
    ("Delete Player", delete_player)
])



home_team_id = ctk.StringVar()
away_team_id = ctk.StringVar()
match_date = ctk.StringVar()
home_score = ctk.StringVar()
away_score = ctk.StringVar()
match_id = ctk.StringVar()

create_section("🏆 Match Details", [
    ("Match ID:", match_id, "e.g. 1"),
    ("Home Team ID:", home_team_id, "e.g. 1"),
    ("Away Team ID:", away_team_id, "e.g. 2"),
    ("Match Date:", match_date, "YYYY-MM-DD"),
    ("Home Score:", home_score, "e.g. 3"),
    ("Away Score:", away_score, "e.g. 2"),
], [
    ("Add Match", add_match),
    ("Update Match", update_match),
    ("Delete Match", delete_match)
])



view_wrapper = ctk.CTkFrame(scrollable_frame, fg_color="transparent")
view_wrapper.pack(pady=10, fill="both")
view_section = ctk.CTkFrame(view_wrapper, width=700, corner_radius=12)
view_section.pack(pady=10)
view_section.pack_propagate(False)
ctk.CTkLabel(view_section, text="📋 View Players with Teams", font=ctk.CTkFont(size=18, weight="bold")).pack(pady=10)
ctk.CTkButton(view_section, text="Load Players", command=view_players).pack(pady=10)
ctk.CTkLabel(view_section, text="📋 View Coaches with Teams", font=ctk.CTkFont(size=18, weight="bold")).pack(pady=10)
ctk.CTkButton(view_section, text="Load Coaches", command=view_coaches).pack(pady=10)

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