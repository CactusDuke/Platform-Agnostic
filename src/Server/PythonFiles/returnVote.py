#Cacluates votes
import psycopg2
from datetime import datetime

def votePercent():
    conn = psycopg2.connect(database="popvote",
                            host="LOCALHOST",
                            user="python",
                            password='Password',
                            port="5432")
    cursor = conn.cursor()


    cursor.execute(f"SELECT COUNT(v_id), COALESCE(SUM(v_vote), 0) FROM cur_table;")
    vals = cursor.fetchone()

    return(round(vals[1] / vals[0], 2))

if __name__ == "__main__":
    x = votePercent()