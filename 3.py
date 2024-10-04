import sqlite3

con = sqlite3.connect('ЗАДАНИЕ 3.db')
cursor = con.cursor()
name = input('Введите название')
cursor.execute("SELECT * FROM medicines WHERE name=(?)", (name,))
print(cursor.fetchall())