import sqlite3

# создает базу данных
conn = sqlite3.connect('name.db')
# создаем объект cursor который позволяет нам взаимодействовать с бозой данных
cursor = conn.cursor()
# создаем таблицу с двумя текстовыми колонками
cursor.execute('''CREATE TABLE IF NOT EXISTS tab_1(id INTEGER PRIMARY KEY AUTOINCREMENT, col_1 TEXT, col_2 TEXT) ''')
# заполняем таблицу данных

cursor.execute('''INSERT INTO tab_1(col_1,col_2) VALUES ('hello','world')''')
conn.commit()

d = "red"
f = "black"
cursor.execute('''INSERT INTO tab_1(col_1,col_2) VALUES (?,?)''',(d,f))
conn.commit()

# k = 'yyy'
# cursor.execute('''INSERT INTO tab_1(col_1,col_2) VALUES ('q',?)''',(k,))
# conn.commit()
# *
cursor.execute('''SELECT * FROM tab_1''')
k = cursor.fetchall()
#k = cursor.fetchone()
print(k)


