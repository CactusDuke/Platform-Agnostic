#Wipes current table and moves values to old_tables
#Script to create new vote Table
import psycopg2
from datetime import datetime

conn = psycopg2.connect(database="popvote",
                        host="LOCALHOST",
                        user="python",
                        password='Password',
                        port="5432")


cursor = conn.cursor()

cursor.execute(f"SELECT * FROM cur_table;")

date = datetime.today()
fetched = cursor.fetchall()
if fetched != []:
    tableName = fetched[0][5]
    cursor.execute(f"INSERT INTO history (h_date, hv_table) VALUES ('{date}', '{tableName}')")

for i in fetched:
    cursor.execute(f"INSERT INTO old_tables (v_id, v_date, v_long, v_lat, v_vote, v_table) VALUES ({i[0]}, '{i[1]}', {i[2]}, {i[3]}, {i[4]}, '{i[5]}')")

cursor.execute("TRUNCATE TABLE cur_table;")
conn.commit()
conn.close()



