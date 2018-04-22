#!/usr/bin/python3
try:
    from .postgres import CRUDPostgres, PostgresConnect
except Exception:
    from postgres import CRUDPostgres, PostgresConnect


def run():
    print("::::::::::::::WELCOME TO CRAPPY DATABASE SOFTWARE::::::::::::::")
    print("1. Create new record ")
    print("2. Read from ID ")
    print("3. Update Info ")
    print("4: Delete record ")
    print("5: Count total records so far")

    x = int(input("Enter a valid choice "))

    if x == 1:
        CRUDPostgres.create()
    elif x == 2:
        CRUDPostgres.read_from_id()
    elif x == 3:
        CRUDPostgres.update()
    elif x == 4:
        CRUDPostgres.delete()
    elif x == 5:
        CRUDPostgres.read_all()
    else:
        print("Not a valid choice. Terminating program...")

run()


PostgresConnect.conn.commit()
PostgresConnect.c.close()
PostgresConnect.conn.close()
