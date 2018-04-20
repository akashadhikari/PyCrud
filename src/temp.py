import psycopg2
try:
    from .sqlite import Sort
except Exception:
    from sqlite import Sort

conn = psycopg2.connect("dbname=postgresql_kzemssmd user=postgres password=postgres host=localhost")

c = conn.cursor()

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
c.execute("INSERT INTO custom (id, first_name, last_name, email, phone_number, text, date, "
                "boolean, address, url, image_url) VALUES (%s, %s, %s, %s, %s, %s,%s, %s, %s,%s, %s)",
            (id, first_name, last_name, email, phone_number, text, date, boolean,
                 address, url, image_url))
# Delete
# c.execute("DELETE FROM custom WHERE id=5525245")

# Update
upd_id = input("Enter your ID to update: ")
upd_email = input("Enter Updated Email: ")
c.execute("UPDATE custom SET email=%s WHERE id=%s", (upd_email, upd_id))

# Read
c.execute("SELECT id, first_name, email from custom")

rows = c.fetchall()
print(rows)

# Sorting
temp = []

# Tuple to list conversion for convenience
for tup in rows:
    temp.append(list(tup))
print(temp)


a_list = []

# Appending the unordered list
for each in temp:
    a_list.append(each[0])

Sort.insertion_sort(a_list)

print("***********After Sorting***********")

# print(a_list)

conn.commit()
c.close()
conn.close()
