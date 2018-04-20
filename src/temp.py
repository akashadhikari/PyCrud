import psycopg2
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

c.execute("INSERT INTO custom (id, first_name, last_name, email, phone_number, text, date, "
                "boolean, address, url, image_url) VALUES (%s, %s, %s, %s, %s, %s,%s, %s, %s,%s, %s)",
            (id, first_name, last_name, email, phone_number, text, date, boolean,
                 address, url, image_url))
c.execute("SELECT id, first_name, email from custom")
rows = c.fetchall()
print(rows)
conn.commit()
c.close()
conn.close()
