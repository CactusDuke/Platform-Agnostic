#Script to add new vote 
import psycopg2
from datetime import datetime

def addVote(vote=0, lat=0.0, long=0.0):
    conn = psycopg2.connect(database="popvote",
                            host="LOCALHOST",
                            user="python",
                            password='Password',
                            port="5432")


    cursor = conn.cursor()

    cursor.execute(f"SELECT * FROM cur_table;")
    value = cursor.fetchall()
    v_table = value[0][5]

    #Checks if the starting vote is there
    if value[0][4] == -1:
        #Deletes it if it is
        cursor.execute("TRUNCATE TABLE cur_table;")
        conn.commit


    v_date = str(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    v_long = long
    v_lat = lat
    v_vote = vote

    cursor.execute(f"INSERT INTO cur_table (v_date, v_long, v_lat, v_vote, v_table) VALUES ('{v_date}', {v_long}, {v_lat}, {v_vote}, '{v_table}')")

    conn.commit()
    conn.close()
if __name__ == "__main__":
    addVote(1, 4, 3)
    addVote(1, 4, 3)
    addVote(0, 4, 3)
    addVote(1, 4, 3)
    addVote(0, 4, 3)
    addVote(1, 4, 3)
    addVote(0, 4, 3)
    addVote(0, 4, 3)
    addVote(0, 4, 3)
    addVote(0, 4, 3)
