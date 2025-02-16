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
    result = vals[1] / vals[0]

    cursor.execute(f"SELECT v_table FROM cur_table;")
    name = cursor.fetchone()[0]


    return(round(result, 4), name, int(vals[1]), int(vals[0] - vals[1]))

if __name__ == "__main__":
    x = votePercent()
    print(x)