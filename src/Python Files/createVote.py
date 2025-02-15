#Script to create new vote Table
#Will wipe current table
import psycopg2
from datetime import datetime

conn = psycopg2.connect(database="popvote",
                        host="LOCALHOST",
                        user="python",
                        password='Password',
                        port="5432")


cursor = conn.cursor()

cursor.execute("TRUNCATE TABLE cur_table;")

v_date = str(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
print(v_date)
v_long = 0.0
v_lat = 0.0
v_vote = 0
v_table = "Filler Name"

cursor.execute(f"INSERT INTO cur_table (v_date, v_long, v_lat, v_vote, v_table) VALUES ('{v_date}', {v_long}, {v_lat}, {v_vote}, '{v_table}')")

cursor.execute(f"SELECT * FROM cur_table;")
print(cursor.fetchall())


conn.commit()
conn.close()