"""
The following code is for generates and stores data in a temporary memory'
We have generated a database model with relevant fields.
Below, we have defined custom CRUD functions to show all the data stored in the table, Read, Update and Delete them.

"""

import sqlite3
from models import Aayulogic

"""
first_name => First name of the employee
last_name => Last name of the employee
email => Employee's email
phone_number => Employee's phone number
text => Employee's text bio
date => Employee's date of birth
boolean => Employee's sex - M/F
address => Employee's Address
url => URL to a social account
image_url => Display Image URL

"""

conn = sqlite3.connect(':memory:')  # NOTE: sqlite_YOAGQHYR.db contains fake data with 200 entries

c = conn.cursor()  # cursor object to fetch results

# We know what we are doing here, right? :D
# May be its better to name text=>bio, date=>birth_date, boolean=>gender with address broken up into lat and long

c.execute("""CREATE TABLE employees (
             first_name text(100), 
             last_name text(100),
             email decimal unique,
             phone_number varchar(30),
             text text(255),
             date varchar(20),
             boolean text(10),
             address decimal,
             url varchar,
             image_url blob
             )""")


# Some custom CRUD functions using native SQLite commands

# The 'C' in CRUD
def insert_emp(emp):
    with conn:
        c.execute("INSERT INTO employees VALUES (:first_name, :last_name, :email, :phone_number, :text, :date, "
                  ":boolean, :address, :url,:image_url) ",
              {'first_name': emp.first_name,
               'last_name': emp.last_name,
               'email': emp.email,
               'phone_number': emp.phone_number,
               'text': emp.text,
               'date': emp.date,
               'boolean': emp.boolean,
               'address': emp.address,
               'url': emp.url,
               'image_url': emp.image_url
               })


# The 'R' in CRUD
def show_all():
    c.execute("SELECT * FROM employees")
    return c.fetchall()


# The 'U' in CRUD - Needs more modification
def update_fields(emp, email, text):
    with conn:
        c.execute("""UPDATE employees SET email=:email, text=:text
                  WHERE first_name=:first_name AND last_name=:last_name""",
                  {'first_name': emp.first_name, 'last_name': emp.last_name, 'email': email, 'text': text})
        return c.fetchall()


# The 'D' in CRUD
def remove_emp(emp):
    with conn:
        c.execute("DELETE from employees WHERE first_name=:first_name AND last_name=:last_name",
                  {'first_name': emp.first_name, 'last_name': emp.last_name})
        return c.fetchall()

"""

Some other functions besides CRUD can e defined in such ways:

def get_emps_by_name(last_name):
    c.execute("SELECT * FROM employees WHERE last_name=:last_name", {'last_name': last_name})
    return c.fetchall()

print(get_emps_by_name('Doe'))
"""

# Testing it on arbitrary data
emp1 = Aayulogic('John', 'Doe', 'test@fake.com', '984585485', 'Hello All!', '1996/2/3', 1, 'Biratnagar',
                 'www.fb.com/emp1', 'https://www.python.org/static/community_logos/python-logo-master-v3-TM.png')
insert_emp(emp1)
emp2 = Aayulogic('Ram', 'Doe', 'fake@news.com', '999999999', 'I hate humans.', '1996/12/3', 0, 'Wherenot',
                 'www.fb.com/emp2', 'https://www.python.org/static/community_logos/python-logo-master-v3-TM.png')
insert_emp(emp2)

"""
You can do crud operations like

update = update_fields(emp2, 'akash@sky.com', 'I dont really hate humans')
remove = remove_emp(emp2)
"""

print(show_all())

conn.close()
