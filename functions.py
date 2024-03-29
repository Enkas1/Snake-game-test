import psycopg2


conn_details = {
    "host": "localhost",
    "database": "postgres",
    "user": "postgres",
    "password": "megaine11",
    "port": '5432'
} 

def add_score_to_database(highscore):
    try:
        conn = psycopg2.connect(**conn_details)
        cur = conn.cursor()
        cur.execute("INSERT INTO highscore_list (score) VALUES (%s)", (highscore,))
        conn.commit()
        cur.close()
        conn.close()
        return True
    except psycopg2.Error as e:
        print("Something went wrong, IDK", e)
        return False

def check_highest_score(highscore):
    try:
        conn = psycopg2.connect(**conn_details)
        cur = conn.cursor()
        cur.execute("SELECT MAX(score) FROM highscore_list", (highscore))
        current_max_score = cur.fetchone()[0]
        conn.commit
        cur.close()
        conn.close()
        print(current_max_score)
        return True
    except psycopg2.Error as e:
        print("Something went wrong, IDK", e)
        return False
