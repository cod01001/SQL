import sqlite3

# создает базу данных
test22 = sqlite3.connect('home_work_lesson_2.db')
# создаем объект cursor который позволяет нам взаимодействовать с бозой данных
cursor = test22.cursor()
# создаем таблицу с 1 колонной числовой
cursor.execute('''CREATE TABLE IF NOT EXISTS home_work_lesson_2
(id INTEGER PRIMARY KEY AUTOINCREMENT, col_1 INT) ''')






class problem:


    def rarka(self,a=None,d=None,c=None):

        if a is not None and d is None and c is None:
            cursor.execute('''INSERT INTO home_work_lesson_2(col_1)
            VALUES (3)''')
            test22.commit()
        elif a is not None and type(d) is int:
            cursor.execute('''DELETE FROM home_work_lesson_2 WHERE id = 1 ''')
            test22.commit()
        elif a is not None and d is not None and type(c) is int:
            cursor.execute('''UPDATE home_work_lesson_2 SET col_1 = 77 WHERE id = 3''')
            test22.commit()



x = problem()
x.rarka(5)
cursor.execute('''SELECT * FROM home_work_lesson_2''')
k = cursor.fetchall()
print(k)




















