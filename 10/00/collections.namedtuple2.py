from collections import namedtuple

EmployeeRecord = namedtuple('Employees', 'id, name, age')

import csv
for emp in map(EmployeeRecord._make, csv.reader(open("employees.csv"))):
    print(emp.id, emp.name, emp.age)

import sqlite3
conn = sqlite3.connect('employees.sqlite3')
c = conn.cursor()

#テーブル生成
create_table = '''create table Employees (id integer primary key, name text, age integer);'''
try: c.execute(create_table)
except Exception as e: print(type(e), e)

#レコード生成
c.execute('SELECT COUNT(*) FROM Employees;')
fetch = c.fetchall()
print(fetch)
if 0 == fetch[0][0]:
    with open('employees.csv') as f:
        reader = csv.reader(f)
        header = next(reader)
        for row in reader:
            print(row)
            c.execute(f"insert into Employees(id,name,age) values ({row[0]},'{row[1]}',{row[2]});")
        conn.commit()
        print('レコード作成！')

#レコード→namedtuple
c.execute('SELECT id, name, age FROM Employees;')
fetch = c.fetchall()
print(fetch)
for emp in map(EmployeeRecord._make, fetch):
    print(emp.id, emp.name, emp.age)

conn.close()
