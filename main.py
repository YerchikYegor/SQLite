import sqlite3

con = sqlite3.connect("data.db")
cursor = con.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS tea
                (id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                age INTEGER DEFAULT 0)
                """)

#cursor.execute("""DROP TABLE tea""")
#
#cursor.execute("""DROP TABLE IF EXISTS users""")

cursor.execute("INSERT INTO tea (name, age) VALUES ('Tom', 37)")
cursor.execute("INSERT INTO tea (name, age) VALUES (?,?) ",('Tom', 37))
con.commit()

cursor.execute("INSERT INTO tea (name, age) VALUES ('Tom', 38), ('Bob', 40), ('Anna', 35)")
con.commit()