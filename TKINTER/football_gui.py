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
