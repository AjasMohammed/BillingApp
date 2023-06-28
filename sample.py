import sqlite3


conn = sqlite3.connect("pybill.db")

cursr = conn.cursor()

# cursr.execute("""CREATE TABLE IF NOT EXISTS class(
#                 std_id INTEGER PRIMARY KEY AUTOINCREMENT,
#                 name TEXT
# )""")


# cursr.execute("DELETE FROM users")

conn.commit()
cursr.execute("SELECT company FROM users WHERE username=?",("Ajas Mohammed",))

row = cursr.fetchall()

for i in row:
    print(i)

cursr.close()
conn.close()