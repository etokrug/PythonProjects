import unittest
from classFactory import build_row
import mysql.connector
from database import login_info

class DBTest(unittest.TestCase):
    
    def setUp(self):
        C = build_row("user", "id name email")
        self.c = C([1, "Steve Holden", "steve@holdenweb.com"])
    
    def test_attributes(self):
        self.assertEqual(self.c.id, 1)
        self.assertEqual(self.c.name, "Steve Holden")
        self.assertEqual(self.c.email, "steve@holdenweb.com")
    
    def test_repr(self):
        self.assertEqual(repr(self.c),
                         "user_record(1, 'Steve Holden', 'steve@holdenweb.com')")
    
    def test_retrieve_data_row_objects(self):
        db = mysql.connector.Connect(**login_info)
        cursor = db.cursor()
        table = 'animal'
        cols = 'id name family weight'
        D = build_row(table, cols)
        sql = 'select * from animal;'
        cursor.execute(sql)
        expected_rows = set()
        for row in cursor.fetchall():
            expected_rows.add(repr(D(row)))
        
        d = D([100, "Joe", "Python", 10])
        observed_rows = set()
        for row in d.retrieve(cursor):
            observed_rows.add(repr(row))
        
        self.assertEqual(observed_rows, expected_rows)

if __name__ == "__main__":
    unittest.main()