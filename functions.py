import psycopg2
from tkinter import *
from tkinter import Toplevel

conn_details = {
    "host": "localhost",
    "database": "postgres",
    "user": "postgres",
    "password": "Change this",
    "port": '5432'
} 

def add_player_and_score(player_name, score):
    try:
        conn = psycopg2.connect(**conn_details)
        cur = conn.cursor()
        
        # Check if the player exists
        cur.execute("SELECT id FROM players WHERE name = %s", (player_name,))
        player_row = cur.fetchone()
        
        if player_row:
            # Player exists, update their score
            player_id = player_row[0]
            cur.execute("UPDATE highscores SET score = %s WHERE player_id = %s AND score < %s", (score, player_id, score))
        else:
            # Player doesn't exist, insert them and their score
            cur.execute("INSERT INTO players (name) VALUES (%s) RETURNING id", (player_name,))
            player_id = cur.fetchone()[0]
            cur.execute("INSERT INTO highscores (player_id, score) VALUES (%s, %s)", (player_id, score))

        conn.commit()
        cur.close()
        conn.close()
        return True
    except psycopg2.Error as e:
        print("Error", e)
        return False
    
def show_high_scores(window):
    try:
        conn = psycopg2.connect(**conn_details)
        cur = conn.cursor()
        cur.execute("SELECT * FROM sorted_score_list LIMIT 10")
        high_scores = cur.fetchall()
        cur.close()
        conn.close()
        
        # Display high scores in a new window or dialog
        high_scores_window = Toplevel(window)
        high_scores_window.title("High Scores")

        high_scores_window.geometry("1000x600")
        
        # Create a label to display the high scores
        label = Label(high_scores_window, text="High Scores", font=("consolas", 14))
        label.pack()
        
        # Display fetched high scores
        for idx, (player_name, score) in enumerate(high_scores, start=1):
            score_label = Label(high_scores_window, text=f"{idx}. {player_name}: {score}")
            score_label.pack()
    except psycopg2.Error as e:
        print("Something went wrong :(", e)
