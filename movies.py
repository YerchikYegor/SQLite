import sqlite3

con = sqlite3.connect("data.db")
cursor = con.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS movies
                (название TEXT,
                рейтинг REAL,
                год INTEGER,
                режиссер TEXT,
                жанр TEXT)
                """)

#cursor.execute("""DROP TABLE tea""")
#
#cursor.execute("""DROP TABLE IF EXISTS users""")

cursor.execute("INSERT INTO movies (название, рейтинг, год, режиссер, жанр) VALUES ('1+1', 8.8, 2011,'Оливье Накаш, Эрик Толедано', 'драмма')")
cursor.execute("INSERT INTO movies (название, рейтинг, год, режиссер, жанр) VALUES ('Брат', 8.3, 1997,'Алексей Балабанов', 'драмма')")
con.commit()
