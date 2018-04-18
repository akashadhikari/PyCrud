"""
The following code is for testing the fake data which is stored on custom database 'sqlite_YOAGQHYR.db'
Here, we have generated a database with relevant fields with up to 200 entries.
Below, we have defined a custom function to show all the data stored in the table.

Method for generating fake data using fake2db:

fake2db --rows 200 --db sqlite --custom first_name last_name email phone_number text date boolean address url image_url

"""
import sqlite3
import unittest


conn = sqlite3.connect('sqlite_YOAGQHYR.db')

c = conn.cursor()


def show_all():
    c.execute("SELECT * FROM custom")
    return c.fetchall()


"""
Testing the number of entries on the database.
"""


class TestNumber(unittest.TestCase):

    def test_number_of_entries(self):
        self.assertEqual(len(show_all()), 200)


if __name__ == '__main__':
    unittest.main()

conn.close()
