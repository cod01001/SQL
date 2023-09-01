import sqlite3

#создал таблицу
lesson_3 = sqlite3.connect('lesson_3.db')

#создаем обьект через который бедм взаимодйствовать с базой данных
cursor = lesson_3.cursor()

# создаем таблицу и прописываем в ней колонки, их количество название и тип данных
cursor.execute('''CREATE TABLE IF NOT EXISTS home_work_lesson_2_task_5 
(id INTEGER PRIMARY KEY AUTOINCREMENT, col_1 TEXT,col_2 TEXT)''')


# # заполняем таблицу данных первое значение
# cursor.execute('''INSERT INTO home_work_lesson_2_task_5 (col_1,col_2)
# VALUES ('first','second')''')
# lesson_3.commit()
#
# # заполняем таблицу данных второе значение
# cursor.execute('''INSERT INTO home_work_lesson_2_task_5 (col_1,col_2)
# VALUES ('первый','второй')''')
# lesson_3.commit()
#
# #заполняем таблицу данных третье значение
# cursor.execute('''INSERT INTO home_work_lesson_2_task_5 (col_1,col_2)
# VALUES ('uno','dos')''')
# lesson_3.commit()


# # удаляем 2 строку из таблицы
cursor.execute('''DELETE FROM home_work_lesson_2_task_5 WHERE id = 2''')
lesson_3.commit()

# меняем значение в 3 стоблике на hello world
cursor.execute('''UPDATE home_work_lesson_2_task_5 
SET col_1 = 'hello' , col_2 = 'world' WHERE id = 3 ''')
lesson_3.commit()


cursor.execute('''SELECT * FROM home_work_lesson_2_task_5''')
r = cursor.fetchall()

with open('с золотыми волосами.txt', 'w', encoding='utf-8') as file:
    for i in r:
        formatted = ", ".join(str(element) for element in i)
        print(formatted)
        file.write(formatted+'\n')









