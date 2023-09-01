import sqlite3
import random

# создает базу данных
test14 = sqlite3.connect('task_2.db')
# создаем объект cursor который позволяет нам взаимодействовать с бозой данных
cursor = test14.cursor()
# создаем таблицу с двумя текстовыми колонками
cursor.execute('''CREATE TABLE IF NOT EXISTS task_2
(id INTEGER PRIMARY KEY AUTOINCREMENT, col_1 INT, col_2 INT) ''')

x = random.randint(0, 9)
x2 = random.randint(0, 9)

# заполняем таблицу данных
# cursor.execute('''INSERT INTO task_2(col_1,col_2)
# VALUES (?,?)''',(x,x2))
# test14.commit()

cursor.execute('''SELECT * FROM task_2''')
r = cursor.fetchall()

print(r)
rand = random.choice(r)
print(rand)

if rand[1] % 2 == 0 and rand[2] % 2 == 0:
    print('четное')
    cursor.execute('''DELETE FROM task_2 WHERE id = ? ''', (rand[0],))
    test14.commit()
elif rand[1] % 2 != 0 and rand[2] % 2 != 0:
    print('нет')
    cursor.execute('''UPDATE task_2 SET col_1 = 2,col_2 = 2 WHERE id = ? ''', (rand[0],))
    test14.commit()

cursor.execute('''SELECT * FROM task_2''')
r = cursor.fetchall()

print(r)

# r2 = 0
# for i in range(len(r)):
#     for i2 in range(len(r[0])):
#         r2 += (r[i][i2])
#
# m = r2 / (len(r) * 2)
# print(m)
#
# if m < len(r):
#     cursor.execute('''DELETE FROM task_2 WHERE id = 4 ''')
#     test14.commit()
#
# cursor.execute('''SELECT * FROM task_2''')
# r22 = cursor.fetchall()
# print(r22)
