"""
The following code is for testing the fake data which is stored on custom database 'postgresql_kzemssmd'
Here, we have generated a database with relevant fields with up to 100000 entries.
Below, we have defined a custom function to show all the data stored in the table.

Method for generating fake data using fake2db:

fake2db --rows 100000 --db postgresql --custom first_name last_name email phone_number text date boolean address url image_url

"""

import unittest

import psycopg2


class ConnectTest:
    """
    Setting up test connection.
    """
    conn = psycopg2.connect("dbname=postgresql_kzemssmd user=postgres password=postgres host=localhost")
    c = conn.cursor()

    @staticmethod
    def show_all():
        ConnectTest.c.execute("SELECT * FROM custom")
        return ConnectTest.c.fetchall()


class TestNumber(unittest.TestCase):
    """
    Testing the number of entries on the database.
    """

    def test_number_of_entries(self):
        self.assertGreaterEqual(len(ConnectTest.show_all()), 100000)


if __name__ == '__main__':
    unittest.main()

ConnectTest.conn.close()