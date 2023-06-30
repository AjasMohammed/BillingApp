import sqlite3
import os

file_path = "C:\\Users\\Rahul\\Pybill\\z\\bill_info.db"
conn = sqlite3.connect(file_path)

cursr = conn.cursor()

# cursr.execute("""CREATE TABLE IF NOT EXISTS class(
#                 std_id INTEGER PRIMARY KEY AUTOINCREMENT,
#                 name TEXT
# )""")


# cursr.execute("DELETE FROM users")
# cursr.execute("")

conn.commit()
# cursr.execute("SELECT * FROM bill_info")
# Execute the query to get table names
cursr.execute("SELECT name FROM sqlite_master WHERE type='table';")

row = cursr.fetchall()

for i in row:
    print(i)

cursr.close()
conn.close()