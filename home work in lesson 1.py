import sqlite3

# создает базу данных
test13 = sqlite3.connect('home_work_lesson_1.db')
# создаем объект cursor который позволяет нам взаимодействовать с бозой данных
cursor = test13.cursor()
# создаем таблицу с двумя текстовыми колонками
cursor.execute('''CREATE TABLE IF NOT EXISTS home_work_lesson_1
(id INTEGER PRIMARY KEY AUTOINCREMENT, col_1 TEXT, col_2 TEXT, col_3 INT) ''')

# x = int(input('введи меня целове число: '))
# # заполняем таблицу данных
# cursor.execute('''INSERT INTO home_work_lesson_1(col_1,col_2,col_3)
# VALUES ('hello','world',?)''',(x,))
test13.commit()

cursor.execute('''SELECT * FROM home_work_lesson_1''')
r = cursor.fetchall()
for i in range(len(r)-1):
    for i2 in range(len(r[0])):
        print(r[i][i2])
    print('\n')
