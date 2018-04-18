import sqlite3
from models import Aayulogic


conn = sqlite3.connect(':memory:')  # :memory: or db name

c = conn.cursor()  # cursor object to fetch results

# We know what we are doing here, right? :D

c.execute("""CREATE TABLE employees (
             first text,
             last text,
             salary integer
             )""")


# Some custom CRUD functions using native SQLite commands
def insert_emp(emp):
    with conn:
        c.execute("INSERT INTO employees VALUES (:first, :last, :salary) ",
              {'first': emp.first, 'last': emp.last, 'salary': emp.salary})


def get_emps_by_name(lastname):
    c.execute("SELECT * FROM employees WHERE last=:last", {'last': lastname})
    return c.fetchall()


def update_salary(emp, salary):
    with conn:
        c.execute("""UPDATE employees SET salary=:salary
                  WHERE first=:first AND last=:last""",
                  {'first': emp.first, 'last': emp.last, 'salary': salary})


def remove_emp(emp):
    with conn:
        c.execute("DELETE from employees WHERE first=:first AND last=:last",
                  {'first': emp.first, 'last': emp.last})


# Testing it on arbitrary data
emp1 = Aayulogic('John', 'Doe', 80000)
emp2 = Aayulogic('Ram', 'Doe', 111111)

insert_emp(emp1)
insert_emp(emp2)

emps = get_emps_by_name('Doe')

print(emps)

conn.close()
