import psycopg2


conn_details = {
    "host": "localhost",
    "database": "postgres",
    "user": "postgres",
    "password": "megaine11",
    "port": '5432'
} 

def add_player_and_score(player_name, score):
    try:
       
        conn = psycopg2.connect(**conn_details)
        cur = conn.cursor()
        cur.execute("SELECT id FROM players WHERE name = %s", (player_name,))
        player_row = cur.fetchone()
        if player_row:
            player_id = player_row[0]
            cur.execute("UPDATE highscores SET score = %s WHERE player_id = %s AND score < %s", (score, player_id, score))
        else:
            cur.execute("INSERT INTO players (name) VALUES (%s)", (player_name,))
            player_id = cur.fetchone()[0]

            cur.execute("INSERT INTO highscores (player_id, score) VALUES (%s, %s)", (player_id, score))

        conn.commit()
        cur.close()
        conn.close()
        return True
    except psycopg2.Error as e:
        print("Error:", e)
        return False