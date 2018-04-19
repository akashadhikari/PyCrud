import psycopg2
import pprint

try:
    from .models import Aayulogic
except Exception:
    from models import Aayulogic


class DbPostgresConnect:

    conn_string = "host='localhost' dbname='postgresql_kzemssmd' user='postgres' password='postgres'"
    # print the connection string we will use to connect
    print("Connecting to database\n	->%s" % (conn_string))

    # get a connection, if a connect cannot be made an exception will be raised here
    conn = psycopg2.connect(conn_string)

    # conn.cursor will return a cursor object, you can use this cursor to perform queries
    c = conn.cursor()

    # execute our Query
    c.execute("SELECT * FROM custom")

    # retrieve the records from the database
    records = c.fetchall()

    # print out the records using pretty print
    # note that the NAMES of the columns are not shown, instead just indexes.
    # for most people this isn't very useful so we'll show you how to return
    # columns as a dictionary (hash) in the next example.
    pprint.pprint(records)


class CrudPostgres:

    # The 'C' in CRUD
    def create(emp):
        with DbPostgresConnect.conn:
            DbPostgresConnect.c.execute(
                "INSERT INTO custom VALUES (:id, :first_name, :last_name, :email, :phone_number, :text, :date, "
                ":boolean, :address, :url,:image_url) ",
                {'id': emp.id,
                 'first_name': emp.first_name,
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
    @staticmethod
    def read():
        DbPostgresConnect.c.execute("SELECT * FROM custom")
        return DbPostgresConnect.c.fetchall()

    # The 'U' in CRUD - Needs more modification
    def update(emp, email, text):
        with DbPostgresConnect.conn:
            DbPostgresConnect.c.execute("""UPDATE custom SET email=:email, text=:text
                      WHERE first_name=:first_name AND last_name=:last_name""",
                      {'first_name': emp.first_name, 'last_name': emp.last_name, 'email': email, 'text': text})
            return DbPostgresConnect.c.fetchall()

    # I want the user to UPDATE only the required fields.

    # The 'D' in CRUD
    def delete(emp):
        with DbPostgresConnect.conn:
            DbPostgresConnect.c.execute("DELETE from custom WHERE first_name=:first_name AND last_name=:last_name",
                      {'first_name': emp.first_name, 'last_name': emp.last_name})
            return DbPostgresConnect.c.fetchall()


# new_emp = Aayulogic(1,'John', 'Doe', 'test@fake.com', '984585485', 'Hello All!', '1996/2/3', 1, 'Biratnagar',
#                  'www.fb.com/new_emp', 'https://www.python.org/static/community_logos/python-logo-master-v3-TM.png')
# CrudPostgres.create(new_emp)
