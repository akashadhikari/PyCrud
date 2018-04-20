from __future__ import print_function
import psycopg2


class PostgresConnect:
    conn = psycopg2.connect("dbname=postgresql_kzemssmd user=postgres password=postgres host=localhost")
    c = conn.cursor()


class CRUDPostgres:

    def create():
        print("::::::::::::::WELCOME TO CRAPPY DATABASE SOFTWARE::::::::::::::")
        id = input("Enter your ID: ")
        first_name = input("Enter First Name: ")
        last_name = input("Enter Last Name: ")
        email = input("Enter Email: ")
        phone_number = input("Enter Phone Number: ")
        text = input("Enter Bio: ")
        date = input("Enter Birth Date: ")
        boolean = input("Enter Sex (M/F): ")
        address = input("Enter Address: ")
        url = input("Enter Social Media URL: ")
        image_url = input("Enter Image URL: ")

        # Create
        PostgresConnect.c.execute("INSERT INTO custom (id, first_name, last_name, email, phone_number, text, date, "
                  "boolean, address, url, image_url) VALUES (%s, %s, %s, %s, %s, %s,%s, %s, %s,%s, %s)",
                  (id, first_name, last_name, email, phone_number, text, date, boolean,
                   address, url, image_url))
        print("Successfully inserted! :)")

    def read_from_id():
        # Read
        id_read = input("Enter the ID to view its information")
        PostgresConnect.c.execute("SELECT id, first_name, last_name, email from custom WHERE id=%s",
                                  (id_read,))
        rows = PostgresConnect.c.fetchall()
        print(rows)

    def read_all():
        PostgresConnect.c.execute("SELECT * from custom")
        rows = PostgresConnect.c.fetchall()
        print(rows)

    def update():
        print("Update a record")
        upd_id = input("Enter your ID to update: ")
        upd_email = input("Enter Updated Email: ")
        PostgresConnect.c.execute("UPDATE custom SET email=%s WHERE id=%s", (upd_email, upd_id))
        print("Successfully updated")

    def delete():
        # Delete
        print("Delete a record")
        del_id = input("Enter the ID to be deleted")
        PostgresConnect.c.execute("DELETE FROM custom WHERE id=%s", (del_id,))


class Sort:

    def insertion_sort(array):
        for index in range(1, len(array)):

            # We'll first track the current positional value
            current_value = array[index]

            # We just checked if the index of current position is greater than 0 AND
            # previous positional value is  greater than current
            while index > 0 and array[index - 1] > current_value:
                # if thats the case, sort them
                array[index] = array[index - 1]

                # We just deducted the index by 1
                index = index - 1

            # set the changed index value to current
            array[index] = current_value

    # What if I get a better search algorithm? I'll simply bind it over here.

    def another_better_search_algorithm(array):
        # How about implementing Count sort or something like that?
        pass


PostgresConnect.c.execute("SELECT * from custom")
rows = PostgresConnect.c.fetchall()

# Some list manipulation to generate
li = []
for row in rows:
    li.append(row)
temp = []
for l in li:
    x = list(l)
    temp.append(x)
array = []
for each in temp:
    array.append(each[0])
print(type(array))

Sort.insertion_sort(array) # Now, we have a sorted array of table IDs using insertion sort

# By now, we have done lots of crazy stuff here. Checkout print(rows), print(li[0:5]), print(temp) or print(array)

anum = 23323232   # number to search for


#  Search for number in array
def binary_search(number, array, lo, hi):

    if hi < lo: return -1       # no more numbers
    mid = (lo + hi) // 2        # midpoint in array
    if number == array[mid]:
        return mid              # number found here
    elif number < array[mid]:
        return binary_search(number, array, lo, mid - 1)     # try left of here
    else:
        return binary_search(number, array, mid + 1, hi)     # try above here


def my_search(anum, array):
    return binary_search(anum, array, 0, len(array) - 1)


pos = my_search(anum, array)
if pos < 0:
    print("not found")
else:
    print("found at position", pos)

PostgresConnect.conn.commit()
PostgresConnect.c.close()
PostgresConnect.conn.close()
