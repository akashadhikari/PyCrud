import sqlite3
from models import Aayulogic


conn = sqlite3.connect(':memory:')  # :memory: or db name

c = conn.cursor()  # cursor object to fetch results

# We know what we are doing here, right? :D
c.execute("""CREATE TABLE employees (
             first text,
             last text,
             salary decimal,
             phone varchar(30),
             bio text,
             birth_date varchar,
             gender text,
             longitude decimal,
             latitude decimal,
             social_media varchar
             )""")


# Some custom CRUD functions using native SQLite commands
def insert_emp(emp):
    with conn:
        c.execute("INSERT INTO employees VALUES (:first, :last, :salary, :phone, :bio, :birth_date, :gender, :longitude,"
                  " :latitude, :social_media) ",
              {'first': emp.first,
               'last': emp.last,
               'salary': emp.salary,
               'phone': emp.phone,
               'bio': emp.bio,
               'birth_date': emp.birth_date,
               'gender': emp.gender,
               'longitude': emp.longitude,
               'latitude': emp.latitude,
               'social_media': emp.social_media
               })


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

"""
:first, :last, :salary, :phone, :bio, :birth_date, :gender, :longitude,"
                  " :latitude, :social_media
"""

# Testing it on arbitrary data
emp1 = Aayulogic('John', 'Doe', 80000.002, '984585485', 'Hello All!', '1996/2/3', 'Male', 27.29, 32.53, 'fb.com/emp1')
emp2 = Aayulogic('Ram', 'Doe', 111111.25, '999999999', 'Heyyy', '1990/1/1', 'Male', 27.2099, 32.5875453, 'fb.com/emp2')


insert_emp(emp1)
insert_emp(emp2)

emps = get_emps_by_name('Doe')

print(emps)

conn.close()
